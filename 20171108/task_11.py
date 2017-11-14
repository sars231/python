#!/usr/bin/python
#coding:utf-8
"""
利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
"""

sstr=raw_input("输入一个字符串：")
def shunxu(n):
    if n==-1:
        return " "
    else:
        return sstr[n]+shunxu(n-1)

print shunxu(len(sstr)-1)


