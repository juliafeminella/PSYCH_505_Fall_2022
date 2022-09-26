# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 01:38:42 2022

@author: Julia
"""
#Operation exercises
print(5/2)
print(5.0/2.0)
# There was no difference between the operations

print (7 % 2)
print(10 % 2)
print (235 % 4)

#It gives us the remainder of the division of the first number by the second

print (8 ** 2)
print (10 ** 5)

#It exponentiates the first number to the power of the second

print (40 // 3)
print (35 // 8)

#It gives us the result of the division as a whole number, disconsidering the remainder

print(6 + 10 + 9 * 9 / 8)
print(5 + 1 + 1 * 2 / 3)
print(1 + 2 * 5 /2)

#Python does follow the order for operations



#Boolean exercises

print(1 == 1.0)
print("1" == "1.0")

#The frist statement is true because, despite being an interger and a float, the value is the same.
#The second statement is false because by putting the paretheses, we are teliing Pythin that's a string, or text, which does not have a numerical value assigned to it

print(5 == 3+2)
#They are equivalent becuse the operation results in the same value

print(1 == 1.0 or "1" == "1.0" and 5 == 3+2)
print(1 == 1.0 and not "1" == "1.0" and 5 == 3+2)
print(1 == 1.0 or "1" == "1.0" and not 5 == 3+2)
print(1 == 1.0 and not "1" == "1.0" or 5 == 3+2)
print(1 == 1.0 or "1" == "1.0" or 5 == 3+2)



#List exercises
oddlist= [1,3,5,7,9]
#It did become a variable

print(oddlist)

print(len(oddlist))
#5

print(type(oddlist))
#class list

intlist=list(range(100))
print(intlist)



#Dictionary exercises
about_me= {'name': "Julia", 'age': 23.9, 'year_of_study': 2022, 'exp': ['lasagna','cake','gyoza','pastel']}

print(about_me)
print(type(about_me))

print(len(about_me))
#It returns the number of variables within the dicitionary



#Array exercises
import numpy as np

mixnums= np.array([1,2.5,3,5.5,4,1.5])
print(mixnums)
#It created an array of floats

mixtypes= np.array([1,2.5,3,5.5,"nine","six"])
print(mixtypes)
#It created an array of strings. It seems that every element of the array must be of the same type, so Python converts them

oddarray= np.linspace(1, 99, 50)
print(oddarray)

logarray= np.logspace(0.1,0.5, 16)
print(logarray)