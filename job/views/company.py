#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-1-12
from job.models import Company
from job.serializers.company import CompanySerializer
from job.views import BaseModelViewSet


class CompanyViewSet(BaseModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
