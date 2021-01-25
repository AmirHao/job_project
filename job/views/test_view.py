#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ 2021-1-18
import ast

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ViewSet

from job.serializers.test_serializer import TestSerializer
from job.views import BaseModelViewSet
from utils.db import redis_c


class TestAPIView(APIView):

    def get(self, request):
        a = request.query_params.get('a')
        b = request.query_params.get('b')
        if not (a and b):
            raise ValueError('参数缺失')
        c = ast.literal_eval(a) / ast.literal_eval(b)
        return Response('结果是：{}'.format(c))

    def post(self,request):

        return Response('APIView：post 请求')


class TestGenericView(GenericAPIView):
    queryset = None
    serializer_class = TestSerializer

    def get(self, request):
        a = request.query_params.get('a')
        b = request.query_params.get('b')
        if not (a and b):
            raise ValueError('参数缺失')
        c = ast.literal_eval(a) * ast.literal_eval(b)
        return Response('结果是：{}'.format(c))

    def post(self, request):
        return Response('GenericAPIViewSet：post 请求')


class TestViewSet(ViewSet):
    # queryset = None
    # serializer_class = TestSerializer

    def list(self, request):
        a = request.query_params.get('a')
        b = request.query_params.get('b')
        if not (a and b):
            raise ValueError('参数缺失')
        c = ast.literal_eval(a) + ast.literal_eval(b)
        return Response('结果是：{}'.format(c))

    def create(self, request):
        return Response('ViewSet：post 请求')


class TestGenericViewSet(GenericViewSet):
    queryset = None
    serializer_class = TestSerializer

    def list(self, request):
        a = request.query_params.get('a')
        b = request.query_params.get('b')
        if not (a and b):
            raise ValueError('参数缺失')
        c = ast.literal_eval(a) - ast.literal_eval(b)
        return Response('结果是：{}'.format(c))

    def create(self, request):
        return Response('GenericViewSet：post 请求')


class TestModelViewSet(BaseModelViewSet):
    queryset = None
    serializer_class = TestSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        a = serializer.data.get('a')
        b = serializer.data.get('b')
        c = a % b

        request.session['name'] = 'hzm_session_%'
        request.session['value'] = c
        request.session.set_expiry(30)
        return Response('session 储存')

        # redis_key = 'hzm_jisuan_%'
        # redis_c.set(redis_key, c, ex=30)
        # return Response('结果是：{}'.format(c))

    def create(self, request, *args, **kwargs):
        a = request.session.get("name")
        b = request.session.get("value")
        return Response(f'{a}{b}')

        # redis_key = 'hzm_jisuan_%'
        # res = redis_c.get(redis_key)
        # return Response(f'BaseModelViewSet：post 请求{res}')
