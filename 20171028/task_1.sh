#!/bin/sh
i=1
while [ $i -lt 255 ];do
	ping 192.168.1.$i | grep llt
	let i=i+1
done
