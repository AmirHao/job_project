#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-1-11
from job.models import Role
from job.serializers.role import RoleSerializer
from job.views import BaseModelViewSet


class RoleViewSet(BaseModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
