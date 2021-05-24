#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-2-1
# from celery import Celery

import time

# from utils.celery import spawn_obj_id
from utils.celery.main import celery_app


@celery_app.task
def sendmail(mail, flag):
    print(f"环境：{flag}")
    print(f"异步邮件: sending mail to {mail}...")
    time.sleep(2.0)
    print(f"异步邮件: sent OK.")
