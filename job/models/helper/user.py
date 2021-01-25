#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-1-19
from job.models.user import User


def check_user(name, mobile):
    user_queryset = User.objects.filter(name=name, mobile=mobile)
    if user_queryset.exists():
        return user_queryset.first()
    return None
