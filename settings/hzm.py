#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-1-19
from settings.base import *     # noqa
from utils.celery.main import celery_app

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'my_project',
        'USER': 'root',
        'PASSWORD': 'PassWord',
        'HOST': 'localhost',
        'PORT': '3306',
        'TEST': {
            'CHARSET': 'utf8mb4',
            'COLLATION': 'utf8mb4_unicode_ci',
        }
    }
}

REDIS = {
    "host": "localhost",
    "port": 6379,
    "password": "",
    "db": 1,
    "encoding": "utf-8"
}

# session的存储配置
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'session'

# 设置session失效时间,单位为秒
SESSION_COOKIE_AGE = 60 * 5

CACHES = {
    "default": {  # 默认
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{REDIS['host']}:{REDIS['port']}/{REDIS['db']}",
        "OPTIONS": {
            # "CLIENT_CLASS": "django_redis.client.DefaultClient",
            # 自动转换为str
            # "CONNECTION_POOL_KWARGS": {"decode_responses": True, "max_connections": 100},
        }
    },
    "session": {  # session
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{REDIS['host']}:{REDIS['port']}/{REDIS['db'] + 5}",
        "OPTIONS": {
            # "CLIENT_CLASS": "django_redis.client.DefaultClient",
            # "CONNECTION_POOL_KWARGS": {"decode_responses": True, "max_connections": 100},
        }
    },
}

CELERY_BROKER_URL = CACHES["default"]["LOCATION"]  # redis作为消息代理

CELERY_RESULT_BACKEND = f"db+mysql://{DATABASES['default']['USER']}:{DATABASES['default']['PASSWORD']}@{DATABASES['default']['HOST']}:{DATABASES['default']['PORT']}/{DATABASES['default']['NAME']}"

CELERY_TIMEZONE = TIME_ZONE

CELERY_ENABLE_UTC = True

# CELERY_TASK_SERIALIZER = 'msgpack'  # 任务序列化和反序列化使用msgpack方案
#
# CELERY_RESULT_SERIALIZER = 'json'  # 读取任务结果一般性能要求不高，所以使用了可读性更好的JSON
#
# CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24  # 任务过期时间
#
# CELERY_ACCEPT_CONTENT = ['json', 'msgpack']  # 指定接受的内容类型

# 有些情况可以防止死锁
CELERYD_FORCE_EXECV = True
# 设置并发worker数量
CELERYD_CONCURRENCY = 20
# 允许重试
CELERY_ACKS_LATE = True
# 每个worker最多执行100个任务被销毁，可以防止内存泄漏
CELERYD_MAX_TASKS_PER_CHILD = 100
# 超时时间
CELERYD_TASK_TIME_LIMIT = 12 * 30

# celery 立即执行
celery_app.conf.update(CELERY_ALWAYS_EAGER=True)
