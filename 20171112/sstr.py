#!/usr/bin/python
#coding:utf-8
"""
打印一个价格小票
"""

width=input("please enter width:")  #设定小票的宽度
price_width=10    
item_width=width-price_width
header_format="%-*s%*s"  #表头项目和宽度，-表示左对齐
format="%-*s%*.2f"  # *表示字段宽度   2f表示精度

print "="*width

print header_format % (item_width,"Item",price_width,"Price")

print "-"*width

print format % (item_width,"Apple",price_width,0.4)
print format % (item_width,"Pear",price_width,0.5)
print format % (item_width,"Cantaloupes",price_width,1.92)
print format % (item_width,"Dried Apricots (16 oz.)",price_width,8)
print format % (item_width,"Prunes(4 lbs.)",price_width,12)

print "="*width

