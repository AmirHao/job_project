#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-1-8
from django.core.validators import RegexValidator

phone_validator = RegexValidator(r"^1[3456789][0-9]{9}$", "请输入正确的手机号码。")
telephone_validator = RegexValidator(r"^(1[3456789][0-9]{9}|(0[0-9]{2,3}\-?)?[2-9][0-9]{6,7})+(\-[0-9]{1,4})?$",
                                     "请输入正确的号码。")
