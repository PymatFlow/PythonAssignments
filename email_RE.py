# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 17:20:11 2019
Assuming that we have some email addresses in the "username@companyname.com" format, 
please write program to print the user name of a given email address. 
Both user names and company names are composed of letters only.
@author: Kz
"""
import re

cdr = re.compile(r'\w+@\w+[.]\w+')

str1 = 'john@google.com'

for item in cdr.finditer(str1):
    print(item.group(0))


"""
Assuming that we have some email addresses in the "username@companyname.com" format, 
please write program to print the company name of a given email address. 
Both user names and company names are composed of letters only. 
"""
cdr2 = re.compile(r'\w+@(\w+)[.](\w+)')

str1 = 'john@google.com'

for item in cdr2.finditer(str1):
    print(item.group(1))



""" 
Write a program which accepts a sequence of words separated by 
whitespace as input to print the words composed of digits only. 
"""

ins = 'program which accepts a'
sp1 = re.split(" ",ins)
for item in sp1:
    if re.match(r'.*\d.*',item):
        print(item)



