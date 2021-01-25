#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-1-8
from django.db import models

from job.models.company import Company
from job.models.helper import BaseModel
from job.models.user import User


class Company2User(BaseModel):
    company = models.ForeignKey(Company, verbose_name='公司', db_column='company_id', db_index=True,
                                on_delete=models.CASCADE, related_name='company2user')
    user = models.ForeignKey(User, verbose_name='公司', db_column='user_id', db_index=True,
                                on_delete=models.CASCADE, related_name='company2user')
    status = models.BooleanField(verbose_name='状态', default=True)
