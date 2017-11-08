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
    if (peo,com) in d_com.items():
        print "people input",peo,", computer input",com,", computer win!"
    if peo==com:
        print "people input",peo,", computer input",com,", pingju!"

import random
i=1
while True:
    print "di",i,"ju"
    peo=raw_input("qingchuquan(shitou/jiandao/bu),input n to over game:")
    if peo=="n":
        break
    com=random.choice(["shitou","jiandao","bu"])
    pan(peo,com)
    i=i+1


    


