#!/usr/bin/python
#coding:utf-8

class hero():
    age=1
    level=1
    shuxing=""
    hp=1000


    def __init__(self,name):
        self.name=name
        print "my name is %s, my level is %d, my blood is %d" %(name,self.level,self.hp)
    def say(self):
        print "my name is",self.name
    def jineng1(self):
        print "释放技能1"
    def jineng2(self):
        print "释放技能2"
    def attack(self,hero):
        print "i am attacking",hero.name
    def attacked(self,hero):
        print "i am attacked by",hero.name
        self.hp=self.hp-200
        print "my blood left",self.hp
    def __str__(self):
        print "str"
        return self.name
h1=hero("鲁班")
h2=hero("后羿")
h1.shuxing="射手"
h1.say()
h1.jineng2()
h1.attack(h2)
h1.attacked(h2)
print h1

h1.__str__()
