cache = {}

def fibonacci(n,cache):
	# Base case
##	print('N is: ', n)
##	print('Cache is: ',cache.items())
	if n <= 1:
		return 1
	if n not in cache:
		cache[n] = fibonacci(n-1,cache) + fibonacci(n-2,cache)
	return cache[n]


print(fibonacci(40,cache))
print(sum(cache.values()))
