#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021/12/21
import random
import time
from turtle import Turtle

from PIL import Image, ImageDraw, ImageFont


def create_seal_template():
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


def create_font():
    images = Image.open("./res.png")
    font = ImageFont.truetype("./Songti.ttc", 16)
    draw = ImageDraw.Draw(images)
    draw.line((12, 56), (255, 0, 0), 10)
    draw.line((100, 56), (255, 0, 0), 10)
    draw.text((30, 30), "上海众简信息技术有限公司", fill=(255, 0, 0), font=font, )
    images.save("./结果.png")

    chinacha = '上海众简信息技术有限公司'
    im = Image.new('RGBA', (400, 300))
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('./Songti.ttc', 30)
    draw.text((10, 120), chinacha, font=font, fill=(110, 0, 255))
    # transfomrdata = (1.1,-0.5,0,-0.5,1.3,0,)
    # im = im.transform((400,300),Image.AFFINE,transfomrdata)
    im.save('./piltest2.png')

    import math, random

    im = Image.open('./piltest2.png', 'r')
    newim = Image.new('RGBA', (400, 300))

    pix = im.load()
    newpix = newim.load()
    w, h = im.size
    # offx = random.randint(5,10) # x方向位移
    # offy = 2  #振幅
    # angley = random.random() #   recommend: 0 ~ 1,  摆动频率
    # 测试下来，修改angley效果最佳，可在0～1之间，或者<50, >50之类出来的效果都还是有的，
    offx = 1
    offy = 0
    angley = 0.6
    for x in range(0, w):
        for y in range(0, h):
            x1 = int(x - offx + offy * math.cos(angley * y))
            if x1 < w and x1 > 0:
                newpix[x1, y] = pix[x, y]

    newim.save('./piltest5.png')


def kou():
    import cv2
    import numpy as np
    src = cv2.imread(r"./fei.png")  # 这里填你的原图像路径
    cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("input", src)
    """
    提取图中的蓝色部分
    """
    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)  # BGR转HSV
    low_hsv = np.array([100, 43, 46])  # 这里要根据HSV表对应，填入三个min值（表在下面）
    high_hsv = np.array([124, 255, 255])  # 这里填入三个max值
    mask = cv2.inRange(hsv, lowerb=low_hsv, upperb=high_hsv)  # 提取掩膜

    # 黑色背景转透明部分
    mask_contrary = mask.copy()
    mask_contrary[mask_contrary == 0] = 1
    mask_contrary[mask_contrary == 255] = 0  # 把黑色背景转白色
    mask_bool = mask_contrary.astype(bool)
    mask_img = cv2.add(src, np.zeros(np.shape(src), dtype=np.uint8), mask=mask)
    # 这个是把掩模图和原图进行叠加，获得原图上掩模图位置的区域
    mask_img = cv2.cvtColor(mask_img, cv2.COLOR_BGR2BGRA)
    mask_img[mask_bool] = [0, 0, 0, 0]
    # 这里如果背景本身就是白色，可以不需要这个操作，或者不需要转成透明背景就不需要这里的操作

    cv2.imshow("image", mask_img)
    cv2.imwrite('label123.png', mask_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    kou()
