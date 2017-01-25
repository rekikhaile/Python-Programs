# Exercise 1
print('Anomalocaris'.find('o'))

# Exercise 2
print('Anomalocaris'.find('r'))

# Exercise 3
print('Waging on the purple drone'.rfind('on'))

# Exercise 4
print('Superficial'.rfind('z'))

# Exercise 5
sentence = 'There\
truly is a dazzling bright world out\
there, waiting for us\
to explore.'

half = len(sentence) // 2
##print(half + sentence[half:].find('a'))
print(sentence.find('a', half))

# Exercise 6
sentence = 'There\
truly is a dazzling bright world out\
there, waiting for us\
to explore.'
half = len(sentence) // 2
print(sentence.rfind('a', 0, half))

# Exercise 7
print('91342391'.strip('913'))

# Exercise 8
print('-== Warning! ==-'.strip('-= '))
      
# Exercise 9
print('-== Error! ==-'.rstrip('-= '))

# Exercise 10
print('-== Success! ==-'.lstrip('-= '))

# Exercise 11
print('Changing your dog for a bird?\
Some dog-lover you are.'.replace('dog', 'cat')
)

# Exercise 12
print('Being bold has some uses.'.replace('o', 'a', 1))

# Exercise 13
print('–== Error! ==–'.upper())

# Exercise 14
print('abraham lincoln'.title())

# Exercise 15
print('rEaDaBlE'.lower())

# Exercise 16
print('first word is capitalized'.capitalize())

# Exercise 17
print('a loooooooooooooooooooong word?'.count('o'))

# Exercise 18
print('100000000000000000000000000000000000000000'.count('0'))

# Exercise 19
sentence = 'Something out of\
nothing? I really doubt we can do it anytime soon..'
print(sentence.count('n', 0, len(sentence) // 2))

# Exercise 20
godzillion = '100000000000000000000000000000000000000000'
first_zero = godzillion.find('0')
rest = first_zero + 1
result = godzillion[:first_zero + 1] +\
         godzillion[rest:].replace('0', '9')

print(result)

# Exercise 21
sentence = 'what,if,we,have,no,choice?....'
print(sentence.rstrip('.').replace(',', ' ').capitalize())
##print(sentence)
##sentence_stripped = sentence.rstrip('.')
##print(sentence_stripped)
##sentence_stripped_replaced = sentence_stripped.\
##                             replace(',', ' ')
##print(sentence_stripped_replaced)
##sentenced_stripped_replaced_capitalized = sentence_stripped_replaced.capitalize()
##print(sentenced_stripped_replaced_capitalized)
##


