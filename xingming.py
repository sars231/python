#!/usr/bin/python
#coding:utf-8

storage={}
storage["first name"]={}
storage["middle name"]={}
storage["last name"]={}

print storage
me="Magnus Lie Hetland"
storage["first name"]["Magnus"]=[me]
storage["middle name"]["Lie"]=[me]
storage["last name"]["Hetland"]=[me]
print storage

def lookup(data,label,name):
    return data[label].get(name)

print type(lookup(storage,"middle name","Lie"))

def store(data,full_name):
    names=full_name.split()
    if len(names)==2:
        names.insert(1,"")
    labels="first name","middle name","last name"
    for label,name in zip(labels,names):
        peaple=lookup(data,label,name)
        if peaple:
            peaple.append(full_name)
        else:
            data[label][name]=[full_name]
store(storage,"Magnus Lie Hetland")
store(storage,"bin yu bo")
