#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-1-18
from django_redis import get_redis_connection

redis_c = get_redis_connection(
    "default",
)
