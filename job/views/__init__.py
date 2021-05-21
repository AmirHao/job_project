#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-1-11

from rest_framework.viewsets import ModelViewSet


class BaseModelViewSet(ModelViewSet):
    def query_params_to_data(self):
        """
        转换 url 上的参数到 body 里面。
        """

        # view.filter_fields 字段不用转换到 `request.data`，需要 pick 出来
        self.rewrite_to_query_params()

        params = self.request.query_params
        try:
            data = {k: params[k] for k in params.keys()}
            return data
        except:  # noqa
            return params

    def rewrite_to_query_params(self):
        """
        兼容 POST 方法查询

        把`view.filter_fields`中的 filter 字段从`request.data`的字段回写到`request.query_params`里面

        """
        fields = getattr(self, "filter_fields", {})
        for field in fields:
            if self.request.data.get(field):
                self.request.query_params._mutable = True
                self.request.query_params[field] = self.request.data[field]

        strtime_range_fields = getattr(self, "strtime_range_fields", [])
        for field in strtime_range_fields:
            if self.request.data.get(field["name"]):
                self.request.query_params._mutable = True
                self.request.query_params[field["name"]] = self.request.data[
                    field["name"]
                ]

    def batch_search(self, request, data, *args, **kwargs):
        limit = data.get("limit")
        page = data.get("page", 1)
        if not limit:
            if data.get("batch_search"):
                limit = 1000
            else:
                limit = 10
        request.query_params._mutable = True
        request.query_params["limit"] = limit
        request.query_params["page"] = page
        return self.list(request, *args, **kwargs)
