# Initialize
my_list = []
print(my_list)
my_list = list()
print(my_list)

## Add element to the end
my_list.append(5)
print(my_list)
my_list.append(3)
print(my_list)
# notice, list can contain various types
my_list.append('Im a string')
print(my_list)

## more operations on lists 
my_list.remove('Im a string')
print(my_list)
print(my_list.index(5))
last = my_list.pop()
print(last)
my_list.insert(1, 10)
print(my_list)
print([1, 1, 2, 1, 3].count(1))

## built-in functions
# inplace
my_list.reverse()
my_list.sort()
# with a return value
my_list_copy = sorted(my_list)
my_list_reversed = reversed(my_list)
n = sum(my_list)
print('sum is', n)
my_max = max(my_list)
my_min = min(my_list)
print ('max is %s, min is %s.' % (my_max, my_min))


## list addition
print([2, 3, 4] + [5, 9, 8])

## check the documentation for more



