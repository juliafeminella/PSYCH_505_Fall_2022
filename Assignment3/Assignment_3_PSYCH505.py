# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 12:24:18 2022

@author: Julia
"""

#Variable operations exercises
##Create variables
sub_code= "sub"
subnr_int= 2
subnr_str= "2"

##Test adding
print(sub_code + subnr_str)
#> Only the string will work because Python can only concatanate string with string


##Create series of outputs
print(sub_code + " " + subnr_str)
print(sub_code + " " + subnr_str*3)
print((sub_code + subnr_str) * 3)
print(sub_code*3 + subnr_str*3)




#List operations exercises
numlist= [1,2,3]
print(numlist*2)

##Create array
import numpy as np
numarr= np.array([1,2,3])
print(numarr*2)

#>When we multiply the list, it's printed twice. When we multiply the array, it multiplies the elements by 2

##Create outputs
strlist= ["do","re","mi","fa"]

print([s1 + s2 for s1, s2 in zip(strlist, strlist)])

print(strlist + strlist)

n = 2
print(list(np.repeat(strlist, 2)))

print(list(zip(strlist, strlist)))



# Zipping exercises
#>Calculating the number of possibilities per clue: 5 pics of faces, 5 pics of houses (5x5=25) that are presented in pairs, and therefore in 2 possible orders (50)
print(5*5*2)

faces= ["face1.png","face2.png","face3.png","face4.png","face5.png"]*5
houses= ["house1.png"]*5 +["house2.png"]*5+["house3.png"]*5+["house4.png"]*5+["house5.png"]*5
cue1= ["cue1"]*25
cue2= ["cue2"]*25

##Possibilities with cue 1
face_house_1= list(zip(faces,houses,cue1))
house_face_1= list(zip(houses,faces,cue1))
all_cue1= face_house_1 + house_face_1

##Possibilities with cue2
face_house_2= list(zip(faces,houses,cue2))
house_face_2= list(zip(houses,faces,cue2))
all_cue2= face_house_2 + house_face_2

##Combining all possibilities
all_orders= all_cue1 + all_cue2
print(all_orders)

##Randomizing
np.random.shuffle(all_orders)
print(all_orders)



#Indexing exercises
##Create string
colors= ["red", "orange", "yellow", "green", "blue", "purple"]

##Print penultimate letter
print(colors[-2])

##Print 3rd and 4th characters of penultimate color
print(colors[-2][2])
print(colors[-2][3])

##Remove color purple
colors.remove(colors[5]) #removes a value from a list 

##Add indigo
colors.insert(5,"indigo")
print(colors)

##Add violet
colors.insert(6,"violet")
print(colors)



#Slicing exercises
##Create list
list100 = list(range(0,101))

##Print first 10 numbers
print(list100[:10])

##print all the odd numbers in the list backwards
print(list100[::-2])

##Print the last four numbers in the list backwards
print(list100[:-5:-1])
print(list100[40:44])

##Are the 40th-44th numbers in the list equal to integers 39-43? Show the Boolean operation 
print(list100[40:44] == range(39,43))
