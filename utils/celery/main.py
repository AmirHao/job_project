#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-2-1
import os

from celery import Celery
from celery.schedules import crontab

# 加载项目配置

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.hzm")
# 实例化selery对象

celery_app = Celery("job_p")
# 加载消息队列的配置
celery_app.config_from_object("utils.celery.config", namespace="CELERY")

# 从django注册的app中，自动识别任务
celery_app.autodiscover_tasks()

celery_app.conf.timezone = "Asia/Shanghai"

celery_app.conf.beat_schedule = {
    "test_email": {  # 测试邮件
        "task": "job.tasks.sendmail",
        "schedule": crontab(minute="*/1"),
        "args": ["asd@qq.com", "test"],
    },
    # "autowithdraw_task": {  # 自动提现检测 每隔五分钟检测一次， 跳过23点~1点
    #     "task": "cdl_api.tasks.autowithdraw_task",
    #     "schedule": crontab(minute="*/5", hour="1-23"),
    #     "args": (),
    # },
    # "auto_generate_service_bill": {  # 每天凌晨23:59 生成当天服务费账单
    #     "task": "cdl_api.tasks.auto_generate_service_bill",
    #     "schedule": crontab(hour=23, minute=59),
    #     "args": (),
    # },
    # "auto_check_transfer_freeze_amount": {  # 每天上午10点检查预支付客户账户余额
    #     "task": "cdl_api.tasks.auto_check_transfer_freeze_amount",
    #     "schedule": crontab(hour=10, minute=0),
    #     "args": (),
    # },
}
