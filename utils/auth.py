#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-1-15
import hashlib
import time

import jwt
from django.conf import settings
from jwt import ExpiredSignatureError
from jwt.exceptions import InvalidKeyError, DecodeError, InvalidTokenError

jwt_conf = settings.JWT_CONFIG


def md5_(_str):
    m = hashlib.md5()
    m.update(_str.encode())
    return m.hexdigest()


def create_token(user_id, name, expires=jwt_conf["access_token_expires"]):
    t = time.time()
    payload = create_payload(user_id, t + expires, name=name)
    token = jwt.encode(
        payload,
        jwt_conf["access_token_secret"],
        algorithm=jwt_conf["jwt_header"]["alg"],
        headers=jwt_conf["jwt_header"],
    )
    if not isinstance(token, str):
        token = token.decode("utf8")
    return dict(tk=token, expAt=t + expires, uId=user_id)


def parse_token(token):
    try:
        payload = jwt.decode(
            token,
            jwt_conf["access_token_secret"],
            verify=True,
            algorithms=jwt_conf["jwt_header"]["alg"],
            leeway=jwt_conf["access_token_leeway"],
        )
    except ExpiredSignatureError:
        return
    except (InvalidKeyError, DecodeError) as ex:
        return
    except InvalidTokenError:
        return
    return payload


def create_payload(uId, exp, **kwargs):
    return dict(uId=uId, exp=exp, **kwargs)


def get_token(authorization):
    if not authorization:
        return
    auth_type = authorization[:7]
    token = authorization[7:].strip()
    if auth_type.lower() != "bearer ":
        return
    return token
