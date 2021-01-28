#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-1-12

DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S%z'

REST_FRAMEWORK = {
    # 'DEFAULT_PARSER_CLASSES': (
    #     'rest_framework.parsers.JSONParser',
    # ),
    # 'DEFAULT_RENDERER_CLASSES': (
    #     'rest_framework.renderers.JSONRenderer',
    # ),
    # 'DEFAULT_FILTER_BACKENDS': (
    #     'utils.filter_backends.MyDjangoFilterBackend',
    #     'utils.filter_backends.MySearchFilter',
    #     'utils.filter_backends.MyOrderingFilter'
    # ),
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'utils.permissions.MyBasePermission',
    #     'rest_framework.permissions.IsAuthenticated'
    # ),
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'utils.authentication.JWTAuthentication',
    # ),
    'DEFAULT_PAGINATION_CLASS': 'utils.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': DATETIME_FORMAT,
    # 'EXCEPTION_HANDLER': 'utils.exceptionhandler.exception_handler',
    'EXCEPTION_HANDLER': 'utils.exceptions.custom_exception_handler',
    # 'DEFAULT_SCHEMA_CLASS': 'utils.schemas.BaseSchema',
    # 'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    # 'TEST_REQUEST_RENDERER_CLASSES': (
    #     'rest_framework.renderers.JSONRenderer',
    # ),
    # 'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    # 'DEFAULT_VERSION': '1',
    # 'ALLOWED_VERSIONS': ['1', 'v4', 'v5', 'v1'],
    # 'VERSION_PARAM': 'version',
    # 'DEFAULT_THROTTLE_RATES': {
    #     'login_phone_verify': '60/m',
    #     'openapi_sms_verify': '60/m',
    # },
}
