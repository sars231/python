#!/usr/bin/python
#coding:utf-8

"""
打印2~100之间多有的质数
"""

def pan(num):
    i=2
    while i<num:
        if num%i==0:
            return False  #为什么没有这句的时候，仍然会把所有的数打印出来
            break
        i=i+1
#   print num   执行此语句时，为什么什么数都能打印出来
    return True  #而执行此语句时能正确区分质数
    
for num in range(2,101):
    if pan(num)==True:
        print num,
