#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-1-11
from rest_framework.serializers import ModelSerializer

from job.models import Role


class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
