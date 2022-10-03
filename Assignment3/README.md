# Variable operations exercise
1. Create three variables: "sub_code", "subnr_int", and "subnr_str". The sub_code should be "sub". Assign the integer 2 to subnr_int, and assign the string "2" to subnr_str. Which form of subnr (int or str) can be added to sub_code to create the output "sub2"? Why don't both work?
#Create variables
sub_code= "sub"
subnr_int= 2
subnr_str= "2"

#Test adding
print(sub_code + subnr_str)

> Only the string will work because Python can only concatanate string with string

2. Use operations to create the following outputs with your variables:"sub 2","sub 222","sub2sub2sub2","subsubsub222"
#Create series of outputs
print(sub_code + " " + subnr_str)
print(sub_code + " " + subnr_str*3)
print((sub_code + subnr_str) * 3)
print(sub_code*3 + subnr_str*3)


# List operations exercises
1. Create a list of numbers [1,2,3] called "numlist". Multiply the list by 2.
numlist= [1,2,3]
print(numlist*2)

2. Create a numpy array of numbers [1,2,3] called "numarr". Multiply the array by 2. What is the difference between multiplying lists and multiplying arrays?
#Create array
import numpy as np
numarr= np.array([1,2,3])
print(numarr*2)

> When we multiply the list, it's printed twice. When we multiply the array, it multiplies the elements by 2

3. Create a list of strings ['do','re','mi','fa'] called "strlist". Use operations to create the following outputs with your variable:['dodo','rere','mimi','fafa']
['do','re','mi','fa','do','re','mi','fa']
['do','do','re','re','mi','mi','fa','fa']
[['do','do'],['re','re'],['mi','mi'],['fa','fa']]
#Create outputs
strlist= ["do","re","mi","fa"]

print([s1 + s2 for s1, s2 in zip(strlist, strlist)])

print(strlist + strlist)

n = 2
print(list(np.repeat(strlist, 2)))

print(list(zip(strlist, strlist)))

# Zipping exercise
Create a script that outputs a counterbalanced list with every face paired with every house, repeated with each possible post-cue. Then, randomize the order of the list.

> Calculating the number of possibilities per clue: 5 pics of faces, 5 pics of houses (5x5=25) that are presented in pairs, and therefore in 2 possible orders (50)
faces= ["face1.png","face2.png","face3.png","face4.png","face5.png"]*5
houses= ["house1.png"]*5 +["house2.png"]*5+["house3.png"]*5+["house4.png"]*5+["house5.png"]*5
cue1= ["cue1"]*25
cue2= ["cue2"]*25

#Possibilities with cue 1
face_house_1= list(zip(faces,houses,cue1))
house_face_1= list(zip(houses,faces,cue1))
all_cue1= face_house_1 + house_face_1

#Possibilities with cue2
face_house_2= list(zip(faces,houses,cue2))
house_face_2= list(zip(houses,faces,cue2))
all_cue2= face_house_2 + house_face_2

#Combining all possibilities
all_orders= all_cue1 + all_cue2
print(all_orders)

#Randomizing
np.random.shuffle(all_orders)
print(all_orders)

# Indexing exercises
1. Create a script that outputs a counterbalanced list with every face paired with every house, repeated with each possible post-cue. Then, randomize the order of the list.
#Create string
colors= ["red", "orange", "yellow", "green", "blue", "purple"]

2. Using indexing, print the penultimate color.
print(colors[-2])

3. Using indexing, print the 3rd and 4th characters of the penultimate color.
print(colors[-2][2])
print(colors[-2][3])

4. Using indexing, remove the color "purple" and add "indigo" and "violet" to the list instead.
#Remove purple
colors.remove(colors[5]) 

#Add indigo
colors.insert(5,"indigo")
print(colors)

#Add violet
colors.insert(6,"violet")
print(colors)

# Slicing exercises
1. Create a list of numbers 0-100 called "list100".

list100 = list(range(0,101))

2. Using slicing, print the first 10 numbers in the list.

print(list100[:10])

3. Using slicing, print all the odd numbers in the list backwards.

print(list100[::-2])

4. Using slicing, print the last four numbers in the list backwards.

print(list100[:-5:-1])
print(list100[40:44])

5.Are the 40th-44th numbers in the list equal to integers 39-43? Show the Boolean operation you would use to determine the truth value.

print(list100[40:44] == range(39,43))
