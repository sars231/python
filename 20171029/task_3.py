#!/usr/bin/python
"""
task 3
"""

num=input("please input a sanweishu number:")
a=num/100
b=(num-a*100)/10
c=num-a*100-b*10
print "baiweishu is "+str(a)
print "shiweishu is "+str(b)
print "geweishu is "+str(c)

