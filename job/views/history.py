#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-1-28
import json
import traceback

from django.apps import apps
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from job.serializers.history import HistoriesSerializer


class HistoriesViewSet(ViewSet):
    serializer_class = HistoriesSerializer

    @action(methods=['get', ], detail=False, url_path='log', url_name='log')
    def log(self, request):
        serializer = self.serializer_class(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        model_name = request.query_params['model_name']
        # 获取 model
        try:
            object_id = request.query_params['object_id']
            model = apps.get_model(app_label='job', model_name=model_name)
            model_object = model.objects.get(id=object_id)
        except:
            raise ValidationError('请选择正确的内容')

        result = []
        history_old = None
        # 获取 model 的历史记录
        limit = int(request.query_params.get('limit', 10))
        page = int(request.query_params.get('page', 1))
        query = ~Q(history_change_reason='', ) & ~Q(history_related_key='')
        histories = model_object.history.filter(query).order_by('-history_id')
        # 使用 django 分页
        paginator = Paginator(histories, limit)
        total = paginator.count
        total_page = paginator.num_pages
        try:
            histories_page = paginator.page(page)
        except PageNotAnInteger:
            histories_page = paginator.page(1)
        except EmptyPage:
            histories_page = paginator.page(total_page)

        paging = {
            'page': page,
            'limit': limit,
            'total': total,
            'total_page': total_page,
        }

        # 开始对比每次的历史记录
        for history in histories_page:
            data = {
                'history_date': history.history_date,
                'history_change_reason': history.history_change_reason,
                'actions': [],
            }
            try:
                # 新数据展示
                if history.history_related_key:
                    if history.history_change_reason == None:
                        continue
                    # 找出不同的地方
                    history_old = history.prev_record
                    changes = history.get_history_change(history_old=history_old)
                    if changes:
                        data['actions'].extend(changes)

                    # 如果是外键
                    # foreign_key_model_dict = {}
                    # for history_field in model_object.History.history_fields:
                    #     if not '.' in history_field:
                    #         continue
                    #     # foreign_key： 外键-字符串；foreign_key_field：外键字段-字符串
                    #     foreign_key, foreign_key_field = history_field.split('.')
                    #     if foreign_key not in foreign_key_model_dict:
                    #         foreign_key_model_dict[foreign_key] = []
                    #     foreign_key_model_dict[foreign_key].append(foreign_key_field)
                    #
                    # for foreign_key in foreign_key_model_dict:
                    #     # 找出不同部分
                    #     # foreign_key_model: 外键 Model
                    #     foreign_key_model = model_object._meta.get_field(foreign_key).related_model
                    #     related_model_objects_new = foreign_key_model.history.filter(
                    #         history_related_key=foreign_key + '_' + history.history_related_key).last()
                    #     if not related_model_objects_new:
                    #         continue
                    #     related_model_objects_old = None
                    #     if history_old:
                    #         related_model_objects_old = foreign_key_model.history.filter(
                    #             history_related_key=foreign_key + '_' + history_old.history_related_key).last()
                    #     changes = related_model_objects_new.get_history_change(
                    #         history_old=related_model_objects_old, history_fields=foreign_key_model_dict[foreign_key]
                    #     )
                    #     if changes:
                    #         data['actions'].extend(changes)

            except:
                print(traceback.format_exc())
            result.append(data)
        return Response({'results': result, 'paging': paging})
