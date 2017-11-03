#!/usr/bin/python
"""
task 1
"""

while True:
    num=input("please input integer:")
    if num==int(num):
        if num%2==0:
            print "it is oushu"
        else:
            print "it is jishu"
        break
    else:
        num=input("Error, please input again:")



