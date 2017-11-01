#!/bin/bash
##有语法错误  但是我没有检查出来  



function list_alldir()
{
if [ ! -f "$dir" ];then
	ls -a $dir
else
	echo "输入不正确"
}


dir=input"请输入一个目录："
list_alldir $dir
for l in `ls -a $dir`
do
	if [ ! -f $dir/$l and ! "." $dir/$l and ! ".." $dir/$l ];then
		echo "这是一个目录"
		ls $dir/$l
	elif [ -f $dir/$l ];then
		echo "这是一个文件"
		cat $dir/$l
	else
		echo "不知道是什么"

done



