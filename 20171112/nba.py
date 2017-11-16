#!/usr/bin/python
#coding:utf-8
"""
处理nba.csv 的表格

1、 一共有多少球队
2、 平均得分最高的球队，以及最接近平均分的球队。
3、 三分球投的次数最多的qiu dui
"""


fd=open("/home/binyubo/homework/20171112/nba.csv","r")
print fd
print "详细数据如下："
print fd.read()  #阅读整个数据表
fd.seek(0)  #将指针回到开头处
num=fd.read().count("\n")-2
#通过观察数据，发现第一行和最后一行分别为表头和球队的平均数据，可以通过数换行符的个数来确定球队的个数
print "球队个数为：",num

fd.seek(0)
fd.readline()  #首行为表头，去掉该行
mx=0           #设定一个初始的最大值
for l in fd:   #逐行遍历文件fd，l类型为字符串
    if float(l.split(",")[-1])>mx:
        mx=float(l.split(",")[-1])
        qiudui=l.split(",")[1]
print qiudui , mx

fd.seek(0)
pingjun=float(fd.readlines()[-1].split(",")[-1])
print "平均得分为%5.2f" % pingjun

fd.seek(0)
fd.readline()
jiejin=mx-pingjun
for l in fd:
    if abs(float(l.split(",")[-1])-pingjun)<jiejin:
        jiejin=abs(float(l.split(",")[-1])-pingjun)
        qiudui2=l.split(",")[1]
        defen=float(l.split(",")[-1])
print "最接近平均分的球队是",qiudui2,defen

fd.seek(0)
print fd.readline()
mx3=0
for l in fd:
    tp=float(l.split(",")[8])
    n=int(l.split(",")[2])
    if tp*n>mx3:
        mx3=tp*n
        qiudui2=l.split(",")[1]
print "投三分最多的球队是%s,比赛了%d场，共投%5.2f个" % (qiudui2,n,mx3)

fd.close()
