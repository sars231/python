#!/usr/bin/python
"""
task 1
"""

num=input("please input integer:")
while True:
    if num==int(num):
        if num%2==0:
            print "it is oushu"
        else:
            print "it is jishu"
        break
    else:
        num=input("Error, please input again:")



