#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021/12/21
import random
import time
from turtle import Turtle

from PIL import Image, ImageDraw, ImageFont

# 生成背景图片
max_box = (120, 120)
img1 = Image.new('RGBA', max_box)
draw = ImageDraw.Draw(img1)
x, y, r, b = max_box[0] / 2, max_box[0] / 2, max_box[0] / 2, 5
draw.ellipse((x - r, y - r, x + r, y + r), fill=(255, 0, 0, 255))
draw.ellipse((x - r + b, y - r + b, x + r - b, y + r - b), fill=(0, 0, 255, 0))
img2 = Image.open("./星.png")
img2 = img2.resize((int(max_box[0] / 4), int(max_box[0] / 4)), Image.ANTIALIAS)
print(img2.size)
img1.paste(img2, (45, 45))

# 设置字体
# font = ImageFont.truetype(None, 50)
# txt_str = "往后余生".encode("utf-8").decode("latin-1")
# draw.text((6, 6), "txt_str", fill=(255, 0, 0))
# 保存原始版本
img1.save("res.png")
# image.show()
