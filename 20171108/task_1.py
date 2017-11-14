#!/usr/bin/python
#coding:utf-8

i=0
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if a<>b and b<>c and c<>a:
                print a*100+b*10+c,
                i=i+1
    
print i



