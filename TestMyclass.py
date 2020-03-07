# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 10:58:42 2019
117 Define a class which has at least two methods: 
118 getString: to get a string from console input 
119 printString: to print the string in upper case. 
120 Also please include simple test function to test the class methods. 

@author: Kz
"""

class Myclass():
    def __init__(self):
        self.ins =""
        
    
    
    def getString(self):
        self.ins = input("Enter a string =")
        return self.ins
        
    def printString(self):
        print(self.ins.upper)
        

import unittest

class TestMyclass(unittest.TestCase):
    
    def setUp(self):
        myc = Myclass()
        self.mc = myc

    def test_get_String(self):
        myc = self.mc
        myc.ins ="Honi jonoum"
        #self.assertEqual(self.myc.getString(),"Honi jonoum")
        self.assertIsInstance(myc.getString(),str)



if __name__ == '__main__':
    unittest.main()        