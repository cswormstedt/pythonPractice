# 'ab' is short for 'a'ddress 'b'ook

ab = {
	'Swaroop': 'swaroop@mail.com',
	'larry': 'larry@wall.org',
	'Matsumoto': 'matz@mail.com',
	'Spammer': 'spammer@hotmail.com'
}

print("Swaroop's address is", ab['Swaroop'])

# Deleting a key-value pair
del ab['Spammer']

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
	print('contact {} at {}'.format(name, address))

# adding a key-value pair

ab['Bill'] = 'bill@python.org'

if 'Bill' in ab:
	print('\nBill\'s address is', ab['Bill'])
