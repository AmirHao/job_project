import cv2
import numpy as np
from PIL import Image


def drop_wartermark(path, newpath):
    img = cv2.imread(path, 1)
    # img.shape[:3] 则取彩色图片的高、宽、通道。
    hight, width, depth = img.shape[0:3]
    # 裁剪水印坐标为[y0:y,x0:x1]
    cropped = img[int(hight * 0.9):hight, int(width * 0.7):width]
    # cropped = img[hight-49:hight, width-180:width]
    cv2.imwrite(newpath, cropped)
    # 将图片加载为内存对象 参一：完整路径；参二：flag：-1彩色，0灰色，1原有
    imgsy = cv2.imread(newpath, 1)

    # 图片二值化处理，把[200,200,200]~[255, 255, 255]以外的颜色变成0
    # 这个颜色区间就是水印周边的背景颜色
    thresh = cv2.inRange(imgsy, np.array([200, 200, 200]), np.array([255, 255, 255]))
    # #创建形状和尺寸的结构元素 创建水印蒙层
    kernel = np.ones((3, 3), np.uint8)
    # 对水印蒙层进行膨胀操作
    hi_mask = cv2.dilate(thresh, kernel, iterations=10)
    specular = cv2.inpaint(imgsy, hi_mask, 5, flags=cv2.INPAINT_TELEA)
    cv2.imwrite(newpath, specular)

    # 覆盖图片
    imgsy = Image.open(newpath)
    img = Image.open(path)
    img.paste(imgsy, (int(width * 0.7), int(hight * 0.9), width, hight))
    img.save(newpath)


if __name__ == '__main__':
    # 去除水印，暂时不可用
    drop_wartermark("./水印.png", './无水印.png')
