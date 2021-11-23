#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021/10/20
import os

import qrcode
from PIL import Image


def creats_qr_code():
    # 调用qrcode的make()方法传入url或者想要展示的内容
    img = qrcode.make('https://www.baidu.com')
    # 保存
    img.save("ignore_data/二维码.png")


def create_qr_code_2_file():
    img = qrcode.make('http://www.douban.com')
    # 写入文件
    with open('ignore_data/test1.png', 'wb') as f:
        img.save(f)


def convert_inages(path):
    file_size = os.path.getsize(path)
    print(file_size)
    if file_size > 1024 * 1024 * 2:
        image = Image.open(path)

