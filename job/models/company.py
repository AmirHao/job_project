#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-1-8
from django.db import models
from simple_history.models import HistoricalRecords

from job.models import HistoricalModels
from job.models.helper import BaseModel, BaseHistoricalRecords
from job.models.user import User


class Company(BaseModel, BaseHistoricalRecords):
    user = models.ForeignKey(User, verbose_name='用户', db_column='user_id', db_index=True, on_delete=models.CASCADE,
                             related_name='Company')
    name = models.CharField(max_length=20, verbose_name='公司名称')
    mobile = models.CharField(max_length=11, verbose_name='联系电话')
    email = models.EmailField(max_length=128, verbose_name='邮箱', null=True)
    registration_at = models.DateField(verbose_name='注册时间')
    employees_num = models.PositiveIntegerField(default=0, verbose_name='员工数')
    address = models.CharField(max_length=64, verbose_name='公司地址')
    company_profile = models.CharField(max_length=1024, verbose_name='公司简介', null=True)
    history = HistoricalRecords(bases=(HistoricalModels,))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '招聘公司'

    # 需要记录的变更字段设置，如果部分字段的修改不在声明的字段中，导致该条记录实际有修改，单没有查询出来的更改
    # class History:
    #     history_fields = ('user', )