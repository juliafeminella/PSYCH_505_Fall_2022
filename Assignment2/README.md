# Print exercises 
See [Print Exercises](https://github.com/juliafeminella/PSYCH_505_Fall_2022/blob/2d2adaa48e80886778093f45bd54cd91bc2a543a/Assignment2/yourname.py)

# Operation exercises

1. Divide 5/2 (integer format) and 5.0/2.0 (float format). Does python output the same values for these? (You might get a different answer depending on the version of python you are in). If you got a different answer for the two operations, explain why.
```
print(5/2)
print(5.0/2.0)
```
> There was no difference between the operations

2. What does the modulo operator (%) do? Try it out with a few numbers in this format: "x % y" to get an idea.
```
print (7 % 2)
print(10 % 2)
print (235 % 4)
```
> It gives us the remainder of the division of the first number by the second

3. What do these operators do: ** and //? Try them out with a few numbers in this format: "x // y" to get an idea.
```
print (8 ** 2)
print (10 ** 5)
```
> ** exponentiates the first number to the power of the second

```
print (40 // 3)
print (35 // 8)
```
> // gives us the result of the division as a whole number, disconsidering the remainder

4. Does python follow order of operations? Try it out with a few numbers in this format: "a + b + c * d / e"
```
print(6 + 10 + 9 * 9 / 8)
print(5 + 1 + 1 * 2 / 3)
print(1 + 2 * 5 /2)
```
> Python does follow the order for operations

# Boolean exercises

1. Are 1 and 1.0 equivalent? Are "1" and "1.0" equivalent? Why do you think this is?
```
print(1 == 1.0)
print("1" == "1.0")
```
> The first statement is true because, despite being an interger and a float, the value is the same.
> The second statement is false because by putting the paretheses, we are teliing Pythin that's a string, or text, which does not have a numerical value assigned to it

2. Are 5 and (3+2) equivalent?
```
print(5 == 3+2)
```
> They are equivalent becuse the operation results in the same value

3.Write out the statements [Are 1 and 1.0 equivalent?] X [Are "1" and "1.0" equivalent?] X [Are 5 and (3+2) equivalent?] in proper Boolean syntax, in which you replace X with "and", "or", "and not", or "not". List 5 ways to get True as your output.
```
print(1 == 1.0 or "1" == "1.0" and 5 == 3+2)
print(1 == 1.0 and not "1" == "1.0" and 5 == 3+2)
print(1 == 1.0 or "1" == "1.0" and not 5 == 3+2)
print(1 == 1.0 and not "1" == "1.0" or 5 == 3+2)
print(1 == 1.0 or "1" == "1.0" or 5 == 3+2)
```

# List exercises

1.Create a list called "oddlist", listing all of the odd integers between 0 and 10. Did oddlist become a variable?
```
oddlist= [1,3,5,7,9]
```
> It did become a variable

2.Print oddlist. If you get an error message, double check how you created your list.
print(oddlist)

3.When you use the "len" function on oddlist, how long does python say the list is?
```
print(len(oddlist))
```
> 5

4.When you use the "type" function on oddlist, what type of variable does python say oddlist is? If you get something other than a list, double check how you created your list and try again.
```
print(type(oddlist))
```
> class list

5.Create a list called "intlist", listing all of the integers between 0 and 100 -- do not type them all out manually!
```
intlist=list(range(100))
```

6.Print intlist. Does it list all integers between 0 and 100? If not, double check how you created your list.
print(intlist)

# Dictionary exercises
1. Create a dictionary called "about_me" that contains the following information: your name (string format), age (float format), year of study (integer format), and favorite foods in a list (list of strings).
```
about_me= {'name': "Julia", 'age': 23.9, 'year_of_study': 2022, 'exp': ['lasagna','cake','gyoza','pastel']}
```

2. Print about_me. If there are no error messages at this point, double check your variable with the "type" function to make sure you have made a dictionary.
print(about_me)
```
print(type(about_me))
```

3. Check the length of about_me. How does python determine the length of a dictionary?
```
print(len(about_me))
```
> It returns the number of variables within the dicitionary

# Array exercises
1. Create an array called "mixnums" composed of 3 integers and 3 floats. Print the array. What has happened to the array?
mixnums= np.array([1,2.5,3,5.5,4,1.5])
```
print(mixnums)
```
> It created an array of floats

2.Create an array called "mixtypes" composed of 2 integers, 2 floats, and 2 strings. Print the array. What has happened to the array? What does python do to arrays with mixed types?
```
mixtypes= np.array([1,2.5,3,5.5,"nine","six"])
print(mixtypes)
```
> It created an array of strings. It seems that every element of the array must be of the same type, so Python converts them

3.Create an array called "oddarray" of all odd numbers between 0 and 100.
```
oddarray= np.linspace(1, 99, 50)
print(oddarray)
```

4.Create an array called "logarray" of 16 numbers between 1 and 5 that follow a logarithmic distribution. These should not be integers.
```
logarray= np.logspace(0.1,0.5, 16)
print(logarray)
```
