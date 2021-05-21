#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-1-8
import json
import uuid
import traceback

from django.db import models
from django.conf import settings


def get_shared_signature_full_path(full_path):
    return "OK"


class HistoricalModels(models.Model):
    """
    需要执行 migrate：python manage.py migrate --database historical_records --settings=your.dev
    文档：https://django-simple-history.readthedocs.io/en/latest/quick_start.html
    """

    history_related_key = models.CharField(
        default="", max_length=64, verbose_name="用于关联外键的变化", db_index=True
    )

    class Meta:
        abstract = True

    def get_history_change(self, history_old, history_fields=None):
        """获得变更记录"""

        results = []
        # 获得之前的历史记录
        if not history_old:
            return results
        if not history_fields and hasattr(self.instance_type, "History"):
            history_fields = self.instance_type.History.history_fields

        delta = self.diff_against(history_old)
        # 总会返回的字段
        history_labor_income_tax_mode = (
            history_old.labor_income_tax_mode
            if hasattr(history_old, "labor_income_tax_mode")
            else None
        )
        for change in delta.changes:
            # 如果没有配置显示变更字段，也没有指定，则显示所有
            if not hasattr(self.instance_type, "History"):
                history_fields = history_fields or "all"
            if history_fields != "all" and not change.field in history_fields:
                continue
            # 获得中文显示
            field = self.instance_type._meta.get_field(change.field)
            verbose_name = self.instance_type._meta.get_field(
                change.field
            ).verbose_name.title()
            change_old = change.old
            change_new = change.new
            # 如果是 choices，将值转化为中文
            if field.choices:
                choices = dict(field.choices)
                change_old = choices.get(change_old, change_old)
                change_new = choices.get(change_new, change_new)
            # 如果是 oss 地址，拼接 token
            if hasattr(self.instance_type, "oss_url_fields"):
                if change.field in self.instance_type.oss_url_fields:
                    if change_old:
                        change_old = get_shared_signature_full_path(
                            full_path=change_old
                        )
                    if change_new:
                        change_new = get_shared_signature_full_path(
                            full_path=change_new
                        )

            results.append(
                {
                    "history_content": change_old,  # 变更之前内容
                    "current_content": change_new,  # 变更之后内容
                    "field": verbose_name,  # 变更字段
                    "history_detail": {
                        "models_name": self.instance_type._meta.label.split(".")[1],
                        "field_en": change.field,
                        "new_history_id": self.history_id,
                        "old_history_id": history_old.history_id,
                    },
                    "history_labor_income_tax_mode": history_labor_income_tax_mode,
                }
            )

        return results

    def set_history_change_reason(self):
        """
        设置变更记录操作人, 通过上层的 model 赋值 changeReason 时，到了 HistoryModel 会变成 history_change_reason
        history_change_reason   : 变更记录操作人
        history_related_key     : 变更 ForeignKey 关联
        foreign_key_class_name  : 变更 ForeignKey 的字段名
        """
        change_reason_package = {}
        try:
            # 如果封装过的，解析成字典
            changeReason = json.loads(self.history_change_reason)
            history_change_reason = changeReason["history_change_reason"]
            history_related_key = changeReason["history_related_key"]
            foreign_key_class_name = changeReason["foreign_key_class_name"]
        except:
            # 第一次是未封装的，需要后面的封装
            history_change_reason = self.history_change_reason
            history_related_key = uuid.uuid4().hex
            foreign_key_class_name = ""
        if history_change_reason == "@@":
            self.history_change_reason = ""
        else:
            self.history_change_reason = history_change_reason
        change_reason_package["history_change_reason"] = history_change_reason
        # 变更 ForeignKey 关联
        self.history_related_key = (
            foreign_key_class_name + "_" + history_related_key
            if foreign_key_class_name
            else history_related_key
        )
        change_reason_package["history_related_key"] = history_related_key
        return change_reason_package

    def save(self, *args, **kwargs):
        # 如果没有设置变更原因，不记录
        if not self.history_change_reason:
            return
        # 封装变更信息，包括：变更记录操作人；变更 ForeignKey 关联；变更 ForeignKey 的字段名
        change_reason_package = self.set_history_change_reason()
        # 获得使用 history 功能的 model class
        instance_type = self.instance_type
        # 获得使用 history 功能的实例
        instance = self.instance
        # 获得需要显示的 ForeignKey 字段，手动的将 ForeignKey 数据保存一遍
        if hasattr(instance_type, "History"):
            foreign_key_obj_set = set()
            for history_field in instance_type.History.history_fields:
                if not "." in history_field:
                    continue
                # foreign_key_class： ForeignKey 的 class，foreign_key_field： ForeignKey 的 field
                foreign_key_class, foreign_key_field = history_field.split(".")
                if hasattr(instance, foreign_key_class):
                    foreign_key_obj = getattr(instance, foreign_key_class)
                    if not foreign_key_obj:
                        continue
                    change_reason_package["foreign_key_class_name"] = foreign_key_class
                    foreign_key_obj.changeReason = json.dumps(change_reason_package)
                    foreign_key_obj_set.add(foreign_key_obj)
            for foreign_key_obj in foreign_key_obj_set:
                foreign_key_obj.save()
        super().save(*args, **kwargs)

    @staticmethod
    def test_for_change(instance, validated_data):
        try:
            fields_lst = []
            for fields in instance.History.history_fields:
                if "." in fields and (
                    validated_data.get(fields.split(".")[0])
                    and not isinstance(validated_data.get(fields.split(".")[0]), dict)
                ):
                    fields = fields.replace(".", "__")
                fields_lst.append(fields)
            validated_data_fields = []
            for k, v in validated_data.items():
                if isinstance(v, dict) and k not in instance.json_fields:
                    for i in v:
                        validated_data_fields.append(k + "." + i)
                else:
                    validated_data_fields.append(k)
            # 获取validated_data与fields_lst的差集，并忽略
            ignore_fields = list(set(validated_data_fields).difference(set(fields_lst)))
            validated_data_fields = list(
                set(validated_data_fields) - set(ignore_fields)
            )
            is_history = False
            for field in validated_data_fields:
                if "__" in field:
                    field = field.replace("__", ".")
                if (
                    hasattr(instance, "oss_url_fields")
                    and field in instance.oss_url_fields
                ):
                    field_old = getattr(instance, field)
                    field_old = field_old.split("?")[0] if field_old else None
                    field_new = validated_data.get(field, None)
                    field_new = field_new.split("?")[0] if field_new else None
                    if field_old != field_new:
                        is_history = True
                        return is_history
                elif "." in field:
                    related = getattr(instance, field.split(".")[0])
                    if (
                        getattr(related, field.split(".")[1])
                        != validated_data[field.split(".")[0]][field.split(".")[1]]
                    ):
                        is_history = True
                        return is_history
                elif getattr(instance, field) != validated_data[field]:
                    is_history = True
                    return is_history

            return is_history
        except:
            # settings.LLS_LOGGING.error(traceback.format_exc())
            is_history = True
            return is_history
