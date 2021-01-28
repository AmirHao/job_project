from rest_framework import serializers


class HistoriesSerializer(serializers.Serializer):
    model_name = serializers.CharField()
    object_id = serializers.IntegerField()
