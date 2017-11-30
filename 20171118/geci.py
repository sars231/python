#!/usr/bin/python
#coding:utf-8

import csv
l=["红色","黄色","白色","青色","蓝色","紫色","绿色","黑色"]
with open("周杰伦所有歌词.txt","r") as fd:
    txt=fd.read()
    dic={}
    for i in range(0,len(l)):
        dic.update({l[i]:txt.count(l[i])})
    print dic







with open("JAYgeci.csv","w") as csvf:
     spamwriter=csv.writer(csvf, delimiter=",",quotechar="|",quoting=csv.QUOTE_MINIMAL)
     for k,v in dic.items():
         spamwriter.writerow([k,v])

