#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-1-11
from django.db import models

from job.models import JianLi
from job.models.helper import BaseModel
from job.models.helper.enums import job2jianliEnum
from job.models.job import Job


class Job2Jianli(BaseModel):
    job = models.ForeignKey(Job, verbose_name='岗位', db_column='job_id', db_index=True, on_delete=models.CASCADE,
                            related_name='job2jianli')
    jianli = models.ForeignKey(JianLi, verbose_name='简历', db_column='jianli_id', db_index=True,
                               on_delete=models.CASCADE, related_name='job2jianli')
    status = models.IntegerField(verbose_name='状态', choices=job2jianliEnum.choices(), default=job2jianliEnum.default())
