#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-1-7
# Create your models here.
from django.db import models
# from simple_history.models import HistoricalRecords

from job.models.helper import BaseModel, BaseHistoricalRecords
from job.models.role import Role


class User(BaseModel, BaseHistoricalRecords):
    role = models.ForeignKey(Role, verbose_name='角色', db_column='role_id', db_index=True, on_delete=models.CASCADE,
                             related_name='user', default=1)
    name = models.CharField(max_length=20, verbose_name='姓名')
    mobile = models.CharField(max_length=11, verbose_name='手机号', unique=True, help_text='手机号不能重复')
    password = models.CharField(max_length=128, verbose_name='密码', null=False)
    email = models.EmailField(max_length=128, verbose_name='邮箱', null=True)
    # history = HistoricalRecords(bases=(HistoricalModels,), )
