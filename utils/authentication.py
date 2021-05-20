#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-1-19
import jwt
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.exceptions import AuthenticationFailed

from job.models import User
from utils.auth import get_token, parse_token


class WrongTokenExcption(exceptions.APIException):
    status_code = 401


class NoCsrfAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return


class JWTAuthentication(TokenAuthentication, NoCsrfAuthentication):
    def authenticate(self, request):
        authorization = request.META.get('HTTP_AUTHORIZATION') or request.GET.get('Authorization')
        # 校验token是否合法
        token = get_token(authorization)
        payload = parse_token(token)
        if not payload:
            raise WrongTokenExcption('登录超时，请重试')
        # except jwt.ExpiredSignatureError:
        #     raise AuthenticationFailed('过期了')
        # except jwt.DecodeError:
        #     raise AuthenticationFailed('解码错误')
        # except jwt.InvalidTokenError:
        #     raise AuthenticationFailed('不合法的token')
        user = User.objects.filter(id=payload['uId']).filter()
        return user, token

    def enforce_csrf(self, request):
        return


# def get_request_instance(user_info):
#     try:
#         model_class = qs_app_models[user_info['qsApp']]
#         if getattr(model_class, 'employer_field', None):
#             queryset = qs_app_models_objects[user_info['qsApp']].select_related('user', model_class.employer_field)
#         else:
#             queryset = qs_app_models_objects[user_info['qsApp']].select_related('user')
#         instance = queryset.get(user_id=user_info.get('uId'), id=user_info.get('instance_id'))
#     except ObjectDoesNotExist:
#         return None, None
