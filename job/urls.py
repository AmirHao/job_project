#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-1-11

from django.conf.urls import url
from django.urls import path

from job.routers import router
from job.views.hello import *
from job.views.test_view import TestAPIView, TestGenericView, TestViewSet, TestGenericViewSet, TestModelViewSet

urlpatterns = [
    url('hello', hello),
    url('jisuan', jisuan.as_view()),
    path('testapiview', TestAPIView.as_view()),
    path('testgenericapiview', TestGenericView.as_view()),
    # path('testviewset', TestViewSet.as_view({'get': 'list', 'post': 'create'})),
    # path('testgenericviewset', TestGenericViewSet.as_view({'get': 'list', 'post': 'create'})),
    # path('testmodelviewset', TestModelViewSet.as_view({'get': 'list', 'post': 'create'})),
]
urlpatterns += router.urls
