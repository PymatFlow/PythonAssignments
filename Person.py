# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 08:58:37 2019
Define a class Person and its two child classes: 
Male and Female. 
All classes have a method "getGender" which can print "Male" for Male class 
and "Female" for Female class. 
@author: Kz
"""


class Person():
    def __init__(self):
        pass

class Male(Person):
    def __init__(self):
        Person.__init__(self)
        pass
    
    def getGender(self):
        print('Man')

class Female(Person):
    def __init__(self):
        Person.__init__(self)
        pass
    
    def getGender(self):
        print('Female')    
        

pr = Person()
mr = Male()
mr.getGender()
     