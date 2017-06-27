number = 23
running = True

while running:
	guess = int(input('Enter an integer : '))

	if guess == number:
		print('congratulations, you guessed it.')
		# this causes the while loop to stop
		running = False
	elif guess < number:
		print('No, it is a little higher than that.')
	else:
		print('No, it is a little lower than that.')
else:
	print('The while loop is over')
	# do anything else you want to do here

print('Done')