#!/usr/bin/python

def find(l,v):
    for n in l:
        if n==v:
            print "find it"
            return True
    print "not find"
    return False

l=[1,2,3,4,5,6,7,8,9,10,11]

find(l,5)
find(l,12)

