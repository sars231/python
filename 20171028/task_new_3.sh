#!/bin/bash

function list_alldir(){
if [ -f $dir/$l ];then
echo "这是个文件"
cat $dir/$l
elif [ -d $dir/$l ];then
echo "这是个目录"
ls -a $dir/$l
else
echo "不知道是什么"
fi
}

echo "请输入一个目录："
read dir
while [ ! -d $dir ]
do
echo "输入有误，请重新输入："
read dir
done

for l in `ls -a $dir`
do
echo $l
list_alldir
done


