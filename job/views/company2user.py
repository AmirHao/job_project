#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-1-12
from job.models import Company2User
from job.serializers.company2user import Company2UserSerializer
from job.views import BaseModelViewSet


class Company2UserViewSet(BaseModelViewSet):
    queryset = Company2User.objects.all()
    serializer_class = Company2UserSerializer
