#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-1-19
from settings.base import *     # noqa
from utils.celery.main import celery_app

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'my_project',
        'USER': 'root',
        'PASSWORD': '',
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
    "db": 6,
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

# celery 立即执行
celery_app.conf.update(CELERY_ALWAYS_EAGER=True)