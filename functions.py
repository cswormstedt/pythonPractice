def say_hello():
	# block belonging to the function
	print('hello world')
# end of function

say_hello()
say_hello()

def print_max(a, b):
	if a > b:
		print(a, 'is maximum')
	elif a == b:
		print(a, 'is equal to', b)
	else: 
		print(b, 'is maximum')
# end of function

# directly pass literal values
print_max(3, 4)

x = 5
y = 7

print_max(x, y)