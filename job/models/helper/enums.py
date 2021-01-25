#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-1-8
from collections import OrderedDict
from enum import IntEnum


class ChoiceClass(IntEnum):
    __describe__ = OrderedDict()

    @classmethod
    def choices(cls):
        return list(cls.__describe__.items())

    @classmethod
    def choice_dict(cls):
        return cls.__describe__

    @classmethod
    def describe_to_str(cls) -> str:
        return str(dict(cls.__describe__))

    @classmethod
    def get_display(cls, value) -> str:
        """ 获得对应的中文显示 """
        return cls.__describe__.get(int(value), '')


class RoleEnum(ChoiceClass):
    personal = 1
    enterprise = 2
    administrator = 3

    __describe__ = OrderedDict((
        (personal, '个人'),
        (enterprise, '公司'),
        (administrator, '管理员'),
    ))

    @classmethod
    def default(cls):
        return cls.personal


class SexEnum(ChoiceClass):
    males = 1
    females = 2

    __describe__ = OrderedDict((
        (males, '男'),
        (females, '女'),
    ))

    @classmethod
    def default(cls):
        return cls.males


class job2jianliEnum(ChoiceClass):
    to_view = 1
    viewed = 2
    approved = 3
    rejected = 4

    __describe__ = OrderedDict((
        (to_view, '待查看'),
        (viewed, '已查看'),
        (approved, '通过'),
        (rejected, '驳回'),
    ))

    @classmethod
    def default(cls):
        return cls.to_view


class FindJobStatusEnum(ChoiceClass):
    job = 1
    work_job = 2

    __describe__ = OrderedDict((
        (job, '积极找工作'),
        (work_job, '即将离职'),
    ))

    @classmethod
    def default(cls):
        return cls.job
