#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021/12/20
from django.conf import settings
from rest_framework.exceptions import ValidationError

from services import exec_http_req
from utils.log import logger


def call_two_detection(name, id_no):
    payload = {
        "result": {
            "name": name,
            "id_card": id_no,
        },
        "detection_type": 2,
    }
    conf = settings.SERVICE["two_detection"]

    result = exec_http_req(
        url=conf["url"], method=conf["method"], data=payload, headers=conf["headers"]
    )
    if result["status_code"] >= 400:
        raise ValidationError(f"{name}-{id_no} 二要素检测失败，请稍后重试")

    return result["body"]


def two_detection(name, id_no):
    try:
        result = call_two_detection(name, id_no)
    except Exception as ex:
        logger.warning(f"用户：{name}{id_no},二要素检测错误：{ex}")
        return False

    if result["code"] == -1:
        return False
    else:
        if result.get("result"):
            if result["result"].get("msg") == "认证通过":
                return True

    return False
