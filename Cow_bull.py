# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 16:02:54 2019

@author: Kazem Gheysari
"""

import random
random_number = random.randint(1000,9999)
print(random_number)
while(1):
    num_cow,num_bull=0,0
    user_number = input("Guess a four digit number (type exit for exit)= ")
    if user_number == "exit":
        break
    if not len(user_number)==4:
        print("Input invalid")
        continue
    string_random_number = str(random_number)
    if string_random_number==user_number:
        print('  ****  Win  ****')
        break
    for k,n in zip(user_number,string_random_number):
        print(k,n)
        if k==n:
            num_cow=num_cow+1
            continue
        if k in string_random_number:
            num_bull=num_bull+1
    print(str(num_cow)+'  cows, '+str(num_bull)+ '  bulls')    
#def Cow_bull(x):
    