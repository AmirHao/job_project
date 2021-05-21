#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-1-8
from django.db import models

from job.models.helper import BaseModel
from job.models.helper.enums import RoleEnum


class Role(BaseModel):
    # role_choice = (
    #     (1, '个人用户'),
    #     (2, '公司用户'),
    #     (3, '管理员'),
    # ) ['求职者', '招聘者', '管理员']
    name = models.CharField(max_length=32, verbose_name="角色")
    status = models.BooleanField(verbose_name="状态", default=True)
    create_person = models.CharField(max_length=12, verbose_name="创建人", default="")
