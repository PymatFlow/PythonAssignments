# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 11:21:00 2019
Define a class with a generator which can iterate the numbers, 
which are divisible by 7, between a given range 0 and n.
@author: Kz
"""

class Iter7():
    def __init(self):
        self.out=[]
        self.cal7(0)
    
    def cal7(self,N)    :
        out =[]
        for k in range(0,N,7):
            out.append(k)
        self.out = out
        return out    

    def printN(self):
        self.out = self.__init__()
        print(self.out)
        

c7 =  Iter7()

#cff = c7.cal7(65)

c7.printN()