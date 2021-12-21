#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021/12/2

list_a = [4, 2, 6, 8, 9, 5, 7]


def func_(l_):
    for j in range(len(l_)):
        for i in range(len(l_) - 1):
            if l_[i] > l_[i + 1]:
                l_[i], l_[i + 1] = l_[i + 1], l_[i]
            print(l_)
    return l_


print(list_a)
func_(list_a)
