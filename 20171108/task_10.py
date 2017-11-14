#!/usr/bin/python
#coding:utf-8
"""
打印出如下图案（菱形）

    *
   ***
  *****
 *******
  *****
   ***
    *
"""


for i in range(1,8):
    for j in range(1,8):
        if j+i>4 and i-j<4 and j-i<4 and j+i<12:
            print "*",
        else:
            print " ",
    print


