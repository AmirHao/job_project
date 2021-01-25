#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-1-12
from job.models.job import Job
from job.serializers.job import JobSerializer
from job.views import BaseModelViewSet


class JobViewSet(BaseModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
