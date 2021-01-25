#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-1-12
from job.models import JianLi
from job.serializers.jianli import JianLiSerializer
from job.views import BaseModelViewSet


class JianLiViewSet(BaseModelViewSet):
    queryset = JianLi.objects.all()
    serializer_class = JianLiSerializer
