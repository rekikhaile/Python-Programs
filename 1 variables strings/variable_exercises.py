# Exercise 1
miles = 10
feet = 5280
print(miles * feet)

# Exercise 2
hours = 5
minutes = 15
seconds = 4
print(hours * 60 * 60 + minutes\
      * 60 + seconds)

# Exercise 3
width = 5
height = 10
print(2 *(width + height))

# Exercise 4
width = 10
height = 13
print(width * height)

# Exercise 5
pi = 3.14159
r = 15
print(2 * pi * r)

# Exercise 6
pi = 3.14159
r = 10
print(pi * r ** 2)

# Exercise 7
present_value = 1000
annual_rate = 7
years = 5
print(present_value *\
      (1 + 0.01 *annual_rate) * years)

# Exercise 8
first_name = 'Pavel'
last_name = 'Isaev'
name_tag = 'My name is ' + first_name + ' ' +\
           last_name + '.'

print(name_tag)

# Exercise 9
name = 'Pavel'
age = 23
name_and_age = name + ' is ' + str(age) + ' years old.'
print(name_and_age)

# Exercise 10
x0, y0, x1, y1 = 5, 3, 10, 2
distance = ((x0 - x1) ** 2 +\
           (y0 - y1)**2) ** 0.5
print(distance)

# Exercise 11
x0, y0 = 5, 3
x1, y1 = 10, 2
x2, y2 = 7, 5

a = ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5
b = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
c = ((x0 - x2) ** 2 + (y0 - y2) ** 2) ** 0.5
p = 0.5 * (a + b + c)
result = (p * (p - a) * (p - b) * (p - c)) ** 0.5
