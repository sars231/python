#!/usr/bin/python
#coding:utf-8

"""
优化石头剪刀布游戏
"""

def pan(peo,com):
    d_peo={"shitou":"jiandao","jiandao":"bu","bu":"shitou"}
    d_com={"shitou":"bu","jiandao":"shitou","bu":"jiandao"}
    if (peo,com) in d_peo.items():
        print "people input",peo,", computer input",com,", people win!"
        return 1
    if (peo,com) in d_com.items():
        print "people input",peo,", computer input",com,", computer win!"
        return 2
    if peo==com:
        print "people input",peo,", computer input",com,", pingju!"
        return 3

import random
i=1
a=0
b=0
c=0
while True:
    print "di",i,"ju"
    peo=raw_input("qingchuquan(shitou/jiandao/bu),input n to over game:")
    peo=peo.lower()
    peo=peo.strip()
    if "shitou" in peo:
        peo="shitou"
    elif "jiandao" in peo:
        peo="jiandao"
    elif "bu" in peo:
        peo="bu"

    if peo=="n":
        print "people win",a,"ju, computer win",b,"ju, pingju",c,"ju"
        break
    com=random.choice(["shitou","jiandao","bu"])
    j=pan(peo,com)
    if j==1:
        a=a+1
    elif j==2:
        b=b+1
    elif j==3:
        c=c+1

    i=i+1


    


