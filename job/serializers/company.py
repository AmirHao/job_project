#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-1-12
from rest_framework import serializers

from job.models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.history_save()
        validated_data["changeReason"] = "hzm"
        return super().update(instance, validated_data)
