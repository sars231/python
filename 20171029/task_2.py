#!/urs/bin/python

"""
task 2
"""

num=input ("please input a number:")
i=2
j=0
while i < num:
    if num%i==0:
        j=j+1
        break
    i=i+1
if j == 1:
    print "heshu"
else:
    print "zhishu"
