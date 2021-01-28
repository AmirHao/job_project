#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ 2021-1-18
from django.db import DatabaseError
from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # DRF 不会处理的报错
    if isinstance(exc, ZeroDivisionError):
        return Response({'errmsg': '除数不能为零'}, status=500)
    if isinstance(exc, DatabaseError):
        return Response({'errmsg': '数据库错误！'}, status=500)
    if isinstance(exc, ValueError):
        return Response({'errmsg': exc.args}, status=500)

    # 默认使用 DRF 的异常处理模块
    res = exception_handler(exc, context)

    # 其他报错信息
    # if res is None:
    #     view = context['view']  # 出错的视图
    #     error = '服务器内部错误, %s' % exc
    #     print('%s: %s' % (view, error))
    #     return Response({'detail': error}, status=500)

    return res
