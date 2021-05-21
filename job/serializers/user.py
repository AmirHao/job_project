#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-1-11
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import CharField
from rest_framework.serializers import ModelSerializer, Serializer

from job.models import User
from job.models.helper.common import phone_validator
from job.models.helper.user import check_user
from utils.auth import md5_, create_token, parse_token, get_token

PHONE_FIELD = CharField(
    label="手机号码",
    required=True,
    validators=[phone_validator],
    help_text="手机号码",
    error_messages={"required": "请提供手机号码。"},
)


class UserSerializer(ModelSerializer):
    # password = serializers.CharField(min_length=8, max_length=18, help_text='密码', error_messages='密码位数必须在8-18位')

    def create(self, validated_data):
        # user = User(**validated_data)
        # user.set_password(validated_data["password"])
        # user.save()
        pwd = validated_data.get("password")
        if pwd:
            new_pwd = md5_(pwd)
            validated_data["password"] = new_pwd
        user = User.objects.create(**validated_data)
        return user

    class Meta:
        model = User
        fields = "__all__"


class LoginSerializer(Serializer):
    name = CharField(
        label="用户名",
        max_length=20,
        help_text="用户名",
        required=True,
        error_messages={
            "required": "用户名不能为空",
        },
    )
    mobile = PHONE_FIELD

    def create(self, validated_data):
        user = check_user(validated_data["name"], validated_data["mobile"])
        if not user:
            raise ValidationError("用户不存在")
        res_data = create_token(user.id, user.name, expires=600)
        print(res_data)
        return res_data


class LogOutSerializer(Serializer):
    @classmethod
    def logout(cls, athorization):
        token = get_token(athorization)
        if token is None:
            raise ValidationError("未登录")
        user_info = parse_token(token)
        print(user_info)
