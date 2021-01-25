#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-1-8
from django.db import models

from job.models.helper import BaseModel, BaseHistoricalRecords
from job.models.helper.enums import SexEnum, FindJobStatusEnum
from job.models.user import User


class JianLi(BaseModel, BaseHistoricalRecords):
    user = models.ForeignKey(User, verbose_name='用户', db_column='user_id', db_index=True, on_delete=models.CASCADE,
                             related_name='jianli')
    name = models.CharField(max_length=20, verbose_name='姓名')
    mobile = models.CharField(max_length=11, verbose_name='手机号')
    email = models.EmailField(max_length=128, verbose_name='邮箱', null=True)
    gender = models.IntegerField(verbose_name='性别', choices=SexEnum.choices(), default=SexEnum.default())
    age = models.PositiveIntegerField(default=18, verbose_name='年龄')
    national = models.CharField(max_length=20, verbose_name='民族', null=True)
    marriage = models.CharField(max_length=10, verbose_name='婚姻状况', null=True)
    political = models.CharField(max_length=20, verbose_name='政治面貌', null=True)
    education = models.CharField(max_length=20, verbose_name='学历', null=True)
    graduate_school = models.CharField(max_length=20, verbose_name='毕业院校', null=True)
    professional = models.CharField(max_length=20, verbose_name='专业', null=True)
    work_experience = models.CharField(max_length=20, verbose_name='工作经验', default='')
    live_address = models.CharField(max_length=64, verbose_name='居住地址')
    work_address = models.CharField(max_length=64, verbose_name='求职地址', null=True)
    native_place = models.CharField(max_length=64, verbose_name='籍贯', null=True)
    job = models.CharField(max_length=20, verbose_name='岗位')
    salary = models.CharField(max_length=32, verbose_name='薪水')
    status = models.IntegerField(verbose_name='求职状态', choices=FindJobStatusEnum.choices(),
                                 default=FindJobStatusEnum.default())
    work_experienced = models.CharField(max_length=256, verbose_name='工作经历', null=True)
    specialty = models.CharField(max_length=256, verbose_name='特长', null=True)
    is_enable = models.BooleanField(verbose_name='是否启用', default=True)
