for i in range(1, 5):
	print(i)
else:
	print('The for loop is over')


for i in list(range(5)):
	print(i)
else:
	print('the loop is over')


# for (int i = 0; i < 5; i++),\
# in Python you write just:\
# for i in range(0,5)


# while with a break
while True:
	s = input('Enter something : ')
	if s == 'quit':
		break
	print('Length of the string', len(s))
print('done')

# while with a continue
while True:
	s = input('Enter something : ')
	if s == 'quit':
		break
	if len(s) < 3:
		print('Too small')
		continue
	print('Input is of sufficient length')
# Do other kinds of processing here...

