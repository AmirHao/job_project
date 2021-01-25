#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-1-11
from collections import OrderedDict

from rest_framework import serializers
from rest_framework.fields import SkipField
from rest_framework.relations import PKOnlyObject, PrimaryKeyRelatedField


class BaseModelSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):

        ret = OrderedDict()
        fields = self._readable_fields

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            # We skip `to_representation` for `None` values so that fields do
            # not have to explicitly deal with that case.
            #
            # For related fields with `use_pk_only_optimization` we need to
            # resolve the pk value.
            check_for_none = attribute.pk if isinstance(attribute, PKOnlyObject) else attribute
            if check_for_none is None:
                continue
            elif isinstance(field, PrimaryKeyRelatedField):
                ret[field.field_name + '_id'] = field.to_representation(attribute)
            else:
                ret[field.field_name] = field.to_representation(attribute)

        return ret
