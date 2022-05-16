#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzmin
# __date__ = 2022/2/24
import os

print(os.getcwd())


def h_fibonacci(n):
    # 1,1,2,3,5,8,13,21
    a = 1
    b = 1
    print(a, b, end=" ")
    while n > 2:
        a, b = b, a + b
        print(b, end=" ")
        n -= 1


def h_fibonacci2(a, b, n):
    # 1,1,2,3,5,8,13,21
    if n <= 2:
        return 1
    elif n == 3:
        return a + b
    else:
        return h_fibonacci2(b, a + b, n - 1)


if __name__ == '__main__':
    h_fibonacci(10)
    print()
    for k in range(1, 11):
        print(h_fibonacci2(1, 1, k), end=" ")
