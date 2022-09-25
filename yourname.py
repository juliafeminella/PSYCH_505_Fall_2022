# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Printing exercises
print("J")
print("U")
print("L")
print("I")
print("A")

#Variable exercises
##1- Open "yourname.py". Edit the script so that each letter is labeled as a separate variable in this format: letter1, letter2, etc

letter1= 'J'
letter2= 'U'
letter3= 'L'
letter4= 'I'
letter5= 'A'

##2- Run the script. Do any variables show up in the Variable Editor?
#The letters did show up on the Variable Explorer

##3- If there are not any repeated letters in your name: Create a final variable "letterX" that is the same as the first letter of your name. Run the script again. Print letterX and letter1 in the command line. Does python have a problem with two different variables having the same value?
letterX= 'J'
print(letter1)
print(letterX)

#Python does not seem to have a problem with two variables having the same value

##3- If there are not any repeated letters in your name: Create a final variable "letterX" that is the same as the first letter of your name. Run the script again. Print letterX and letter1 in the command line. Does python have a problem with two different variables having the same value?
letterX= 'X'


##5- Give letterX a new letter that is not in your name. Print the new letterX and the other variable(s) that were previously all the same letter. Did changing the value of letterX change the value of the other variable(s)?
print(letter1)
print(letterX)

#Changing the value of letterX did not change the value of the other variable


##6- Redefine letterX with another variable instead of a letter (e.g., letterX=letter1). Print letterX and letter1, one after the other. Now change the value of letter1 to "z". Print letterX and letter1, one after the other. Did changing the value of letter1 change the value of letterX? What does this tell you about python variable assignment?
letterX=letter1
print(letter1)
print(letterX)

letter1= 'Z'
print(letter1)
print(letterX)
#This means that assigning a new value to a variable overrides the previous assignment