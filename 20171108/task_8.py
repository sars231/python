#!/usr/bin/python
#coding:utf-8
"""
讲一个正整数分解质因数
"""

def fenjie(n):
    for i in range(2,n+1):
        if n%i==0:
            print i,
            return fenjie(n/i)

n=raw_input("输入一个正整数：")
fenjie(int(n))
