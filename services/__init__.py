#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021/12/20
import logging
import traceback
from typing import Optional, Dict

import httpx
from httpx._types import RequestFiles  # noqa

from utils.log import logger


def exec_http_req(
        method: str,
        url: str,
        data: Optional[Dict] = None,
        json: Optional[Dict] = None,
        params: Optional[Dict] = None,
        headers: Optional[Dict] = None,
        retry: Optional[int] = 3,
        timeout: Optional[int] = 10,
        files: RequestFiles = None,
):
    headers = dict() if headers is None else headers
    body = dict()
    status_code = 500

    if "application/json" in headers.get("Content-Type", "") and isinstance(data, dict):
        json = data
        data = None

    for i in range(retry):
        try:
            with httpx.Client() as client:
                reply = client.request(
                    method=method,
                    url=url,
                    json=json,
                    files=files,
                    data=data,
                    params=params,
                    headers=headers,
                    timeout=timeout,
                )
                status_code = reply.status_code

                if status_code > 500 and i <= (retry - 1):
                    logger.error(
                        f"retry_call_server method:{method}, "
                        f"url:{url}, params:{params}, json:{json} "
                        f"data:{reply.text}, headers:{reply.headers}",
                    )
                    continue

                logger.info(
                    f"call_server method:{method}, "
                    f"url:{url}, params:{params}, json:{json} "
                    f"data:{reply.text}, headers:{reply.headers}",
                )

                try:
                    body = reply.json()
                except Exception as ex:  # noqa
                    logger.warning(reply.content)
                    body = dict()
                finally:
                    break

        except httpx.RequestError:
            if i == (retry - 1):
                logger.error(traceback.format_exc())
                continue

    return dict(body=body, status_code=status_code)
