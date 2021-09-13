#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021/9/13
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = '使用命令：python manage.py tiyan，启动'

    def handle(self, *args, **options):
        print('主处理程序启动')
        self._something()

    def _something(self):
        print('处理其他事情')
