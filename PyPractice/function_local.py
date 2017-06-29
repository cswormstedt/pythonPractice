x = 50

def func(x):
	print('x is', x)
	x = 2
	print('Changed local x to', x)
# end of function

func(x)
print('x is still', x)

# Default Arguments Values

def say(message, times=1):
	print(message * times)
# end of function

say('Hello')
say('World', 5)

# Keyword Arguments
def func(a, b=5, c=10):
	print('a is', a, 'and b is', b, 'and c is', c)
# end of function

func(3, 7)
func(25, c=24)
func(c=50, a=100)

# VarArgs parameters
def total(a=5, *numbers, **phonebook):
	print('a', a)

	# iterate through all the items in tuple
	for single_item in numbers:
		print('single_item', single_item)

	# inerate through all the items in dictionary
	for first_part, second_part in phonebook.items():
		print(first_part, second_part)
# end of the function

total(10,1,2,3,jack=1123,john=2231,Inge=1560)

# the Return statement
def maximum(x, y):
	if x > y:
		return x
	elif x == y:
		return 'the numbers are equal'
	else:
		return y
# end of function

print(maximum(2, 3))


def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    score_a = 0
    score_b = 0
    # a = (1 if a0 > b0 else 0) + (1 if a1 > b1 else 0) + (1 if a2 > b2 else 0)
    # b = (1 if a0 < b0 else 0) + (1 if a1 < b1 else 0) + (1 if a2 < b2 else 0)
    # return (a,b)









def some_function():
	pass
# end of function

def print_max(x, y);
	'''Prints the maximum of two umbers.

	The two values must be integers.'''
	# convert to integers, in possible
	x = int(x)
	y = int(y)

	if x > y:
		print(x, 'is the maximum')
	else:
		print(y, 'is the maximum')
# end of function
print_max(3, 5)
print(print_max.__doc__)






