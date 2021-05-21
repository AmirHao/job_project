#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-1-12

from django.conf.urls import url

from book.views import BookView

urlpatterns = [
    url(r"books", BookView.as_view()),
]
