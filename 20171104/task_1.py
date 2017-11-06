#!/usr/bin/python
#coding:utf-8

"""
设置一个函数，函数有个一个参数，判断这个数是不是质数
"""

def pan(num):
    i=2
    while i<num:
        if num%i==0:
            return False
            break
        i=i+1
    return True
num=raw_input("请输入一个正整数：")
print pan(int(num))
