#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-1-26
from django.db import models

from job.models.helper import BaseModel


class UserLimit(BaseModel):
    user = models.ForeignKey('job.user', on_delete=models.CASCADE, related_name='user_limit')
    is_enable = models.BooleanField(help_text='是否可用', verbose_name='状态', default=True)

    class Meta:
        verbose_name = '招聘用户'
        # 显示复数会加s，需要加入如下字段；
        verbose_name_plural = verbose_name
