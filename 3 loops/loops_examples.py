# To test each case please comment out the rest of the code before
# running the file

# Basic loop
for i in range(10):
    print(i)

# Same loop with start, end arguments:
# Starts with 5 ends with 9 as 10 is not included
for i in range(5, 10):
    print(i)

# Same loop but now we also add the step argument
# start with 5 and increase i by 2 till we reach 9
for i in  range(5, 10, 2):
    print(i)
    
# Same thing but backwards
for i in range(10, 5, -2):
    print(i)
    
# Another example using a string
my_string = 'This is an example string'
# prints every single letter of the string we're iterating over
for letter in my_string:
    print(letter, end = ' ')

# same thing, but with indices
# notice, that names i and letter are completely arbitrary
for i in range(len(my_string)):
    print(my_string[i], end = ' ')

# now lets move on to while loops
i = 0
while i < 10:
    print(i, end = ' ')
    # do not forget to increment i to avoid infinite loops
    i += 1
# Example with 2 conditions
i = 0
while i < 10 and i != 7:
    print(i, end = ' ')
    i += 1

# Break example, stops when i == 15
for i in range(50):
    print(i)
    if i == 15:
        break
    
# Continue example, does not do anything when i is even
# otherwise prints a number
for i in range(26):
    if i % 2 == 0:
        continue
    print(i)



# Example with input
print() # print a new line
message = input("please enter a message:")
print(message)
while message != 'get me outta here':
    message = input("please enter a message:")
    print(message)



    










    
