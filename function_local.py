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








