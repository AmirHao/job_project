#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-1-12
from rest_framework import serializers

from job.models import Company2User


class Company2UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company2User
        fields = '__all__'
