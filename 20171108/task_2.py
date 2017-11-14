#!/usr/bin/python
#coding:utf-8

"""
一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
"""

import time


for i in range(0,1000):
    for a in range(0,1000):
        for b in range(0,1000):
            if a*a==i+100 and b*b==i+168:
                print i


