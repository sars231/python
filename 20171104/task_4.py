#!/usr/bin/python
#coding:utf-8

"""
写一个函数可以打印字典
用到 k1 --> v1
"""

def print_dict(**c):
    for k,v in c.items():
        print k,"-->",v

print_dict(1="name","2"="age","3"="height")  #为什么不能是数字呢，会显示参数不能是表达式



def echo_stu(**c):
    for k, v in c.items():
        print k, "--->", v
        
echo_stu(name="张三",age=18,h="haha")
