from rest_framework import serializers
from rest_framework.serializers import Serializer


class TestSerializer(Serializer):
    a = serializers.IntegerField(help_text="第一个数", required=True)
    b = serializers.IntegerField(help_text="第二个数", required=True)
