#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-1-8
from django.db import models

from job.models.helper import BaseModel
from job.models.user import User


class Company(BaseModel):
    user = models.ForeignKey(User, verbose_name='用户', db_column='user_id', db_index=True, on_delete=models.CASCADE,
                             related_name='Company')
    name = models.CharField(max_length=20, verbose_name='公司名称')
    mobile = models.CharField(max_length=11, verbose_name='联系电话')
    email = models.EmailField(max_length=128, verbose_name='邮箱', null=True)
    registration_at = models.DateField(verbose_name='注册时间')
    employees_num = models.PositiveIntegerField(default=0, verbose_name='员工数')
    address = models.CharField(max_length=64, verbose_name='公司地址')
    company_profile = models.CharField(max_length=1024, verbose_name='公司简介', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '招聘公司'