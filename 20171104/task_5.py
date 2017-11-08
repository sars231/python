#!/usr/bin/python
#coding:utf-8

"""
打印99乘法表
"""


i=1
j=1
while True:
    for i in range(1,j+1):
        print i,"*",j,"=",i*j,
    j=j+1
    print
    if j==10:
        break



print "-"*100

for i in range(1,10):
    for j in range(1,10):
        if j<=i:
            print i,"*",j,"=",i*j,
    print


