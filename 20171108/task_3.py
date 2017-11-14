#!usr/bin/python
#coding:utf-8

"""
输入某年某月某日，判断这一天是这一年的第几天？
"""

nyr=raw_input("请输入年月日（示例：20171114）：")

year=int(nyr[0:4])
month=int(nyr[4:6])
date=int(nyr[6:])
print year,month,date

month_day1=[31,29,31,30,31,30,31,31,30,31,30,31]

month_day2=[31,28,31,30,31,30,31,31,30,31,30,31]

if month > 1:
    if year%100<>0 and year%4==0:
        day=sum(month_day1[0:month-1])+date
    elif year%400==0:
        day=sum(month_day1[0:month-1])+date
    else:
        day=sum(month_day2[0:month-1])+date
if month==1:
    day=date

print "该日期是该年的第",day,"天"


