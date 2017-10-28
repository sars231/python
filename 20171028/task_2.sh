#!/bin/sh
i=1
num=$i
while [ $i -lt 98 ];
do
	let i=i+2
	let num=num+i
done
sum=$num
	echo "sum=$sum"



