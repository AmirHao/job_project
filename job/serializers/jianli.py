#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-1-12
from rest_framework import serializers

from job.models import JianLi


class JianLiSerializer(serializers.ModelSerializer):
    class Meta:
        model = JianLi
        fields = '__all__'
