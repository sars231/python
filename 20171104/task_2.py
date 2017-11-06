#!/usr/bin/python
#coding:utf-8

"""
设计一个函数，可以输入任意长度的参数，返回参数的个数
"""

def num_(a,*c):
    return len(c)+1

print num_(1,2,3,4,5,6)

