# Conditional exercises

## 1
```
response= 'NaN'

if response == '1' or response == '2':
    print("OK")
elif response == 'NaN':
    print("subject did not respond")
else: print("subject pressed the wrong key")
```
## 2
```
response= '2'

if response == '1' or response == '2':
    print("OK")
    if response == '1' :
        print('Correct!')
    elif response == '2':
        print("Incorrect!")   
elif response == 'NaN':
    print("subject did not respond")
else: print("subject pressed the wrong key")
```

# For loop exercises 
## 1
```
letters = ['J','U','L','I','A']

for letter in letters:
    print(letter)
 ```   
##2
```
letters = ['J','U','L','I','A']

count = -1 #start at -1 to start indexing at 0 within the loop

for letter in letters:
    count = count+1 #every time the loop starts over, add 1 to the count
    
    print(letter)
    print("%i" %count)
```    
## 3
```
list_names = ["Amy","Rory","River"]
for name in list_names:
    for letter in name:
        print(letter)
```    

## 4
```
for name in list_names:
    for letters in name:
        print(letters)
        for let in letters:
            count = count +1
            print(("%s" %count))
```
# Loop exercises
## 1
```
counter = 1
while counter <= 10 : 
    print("image1.png")
    print(counter) 
    
    counter = counter +1

while counter <=20:
    print("image2.png")
    print(counter)
    counter = counter +1
```
## 2
```
response = 2 
valid = False
iteration = 0 #add an iteration counter

while not valid: 
    iteration = iteration +1
    print("Showing an image for %i iterations" %iteration)
    
    if response == 1 or response == 2: 
        valid=True #subject has made a response
```
## 3
```
response = 5
valid = False
iteration = 0 #add an iteration counter
failsafe = -1

while not valid: 
    
    failsafe = failsafe +1 
    if failsafe == 5:
        break
    
    iteration = iteration +1
    print("Showing an image for %i iterations" %iteration)
    
    if response == 1 or response == 2: 
        valid=True #subject has made a response
  ```  
