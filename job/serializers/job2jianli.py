#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-1-12
from rest_framework import serializers

from job.models.job2jianli import Job2Jianli


class Job2JianliSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job2Jianli
        fields = "__all__"
