#!/bin/sh
i=1
num=0
while [ $i -lt 100 ];
do
	let num=num+i
	let i=i+2
done
sum=$num
	echo "sum=$sum"



