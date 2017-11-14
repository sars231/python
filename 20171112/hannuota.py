#!/usr/bin/python
#coding:utf-8

"""
汉诺塔问题
"""

def hnt(n,A,B,C):
    if n==1:
        print A,"-->",B
        return
    else:
        hnt(n-1,A,C,B)
        hnt(1,A,B,C)
        hnt(n-1,B,A,C)


print "n=2"
hnt(2,"A","B","C")
print "n=3"
hnt(3,"A","B","C")
