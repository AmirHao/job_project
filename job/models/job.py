#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-1-11
from django.db import models

from job.models import Company
from job.models.helper import BaseModel


class Job(BaseModel):
    company = models.ForeignKey(Company, verbose_name='企业', db_column='company_id', db_index=True,
                                on_delete=models.CASCADE, related_name='job')
    name = models.CharField(max_length=32, verbose_name='岗位名称')
    work_address = models.CharField(max_length=128, verbose_name='工作地址')
    hiring_num = models.PositiveIntegerField(default=0, verbose_name='招聘人数')
    salary = models.CharField(max_length=32, verbose_name='薪水', null=True)
    Job_description = models.CharField(max_length=256, verbose_name='岗位介绍', default='')
    professional = models.CharField(max_length=20, verbose_name='专业要求', null=True)
    education = models.CharField(max_length=20, verbose_name='学历要求', null=True)
    work_experience = models.CharField(max_length=20, verbose_name='工作经验', default='')
    status = models.BooleanField(verbose_name='状态', default=True)
    contacter = models.CharField(max_length=20, verbose_name='联系人')
    mobile = models.CharField(max_length=11, verbose_name='联系电话')
    email = models.EmailField(max_length=128, verbose_name='邮箱', null=True)
    cerate_person = models.CharField(max_length=20, verbose_name='创建人', default='')
    change_person = models.CharField(max_length=20, verbose_name='修改人', default='')
