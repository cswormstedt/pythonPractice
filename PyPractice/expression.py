length = 5
breadth = 2

area = length * breadth
print('Area is', area)
print('Perimeter is', 2*(length + breadth))


# the if statement is used to check a condition

number = 23
guess = int(input('Enter an integer : '))

if guess == number:
	#New block starts here
	print('Congratulations, you guessed it.')
	print('(but you do not win any prizes!')
	#New block ends here
elif guess < number:
	print('No, it is a little lower than that')
	# you must have guessed > number to reach here

print('Done')
# this last statement is always excuted
# after the if statement is excuted