#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-1-12
from job.models.job2jianli import Job2Jianli
from job.serializers.job2jianli import Job2JianliSerializer
from job.views import BaseModelViewSet


class Job2JianliViewSet(BaseModelViewSet):
    queryset = Job2Jianli.objects.all()
    serializer_class = Job2JianliSerializer
