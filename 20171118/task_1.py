#!/usr/bin/pythhon
#coding:utf-8

def ins(l):
    key=0
    for i in range(1,len(l)):
        key=l[i]
        j=i-1
        while j>=0 and l[j]>key:
            l[j+1]=l[j]
            j=j-1
        l[j+1]=key

l=[4,8,3,9,10,1]
ins(l)
print l


