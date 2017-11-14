#!/usr/bin/python
#coding:utf-8
"""
有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
"""

def num(m):
    if m==1 or m==2:
        return 2
    return num(m-1)+num(m-2)
        

m=raw_input("请输入月数：")

print num(int(m))


