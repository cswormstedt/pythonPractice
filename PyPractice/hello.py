# print is a function
print("hello world") 


age = 25
name = 'Chris'

print('{0} was {1} years old when he wrote this wook'.format(name, age))
print('why is {0} palying with that python?'.format(name))

# decimal (.) precision of 3 for float '0.333'
print('{0:.3f}'.format(1.0/3))

# fill with underscores (_) with the text centered
# (^) to 11 witdth '___hello___'
print('{0:_^11}'.format('hello'))

# keyword-based  'Chris wrote a Byte of Python'
print('{name} is reading {book}'.format(name='Chris', book='A Byte of Python'))


# 'this isn\'t where I parked my car
# 'this is the first line\nThis is the second line'
# \n to indicate the start of a new line
# \t places a tab

print('yo it\'s andre 3000')
print('this is the first line\nThis is the second line')
print('chris\tswormstedt')

# raw strings when dealing with regular expressions

r"Newlines are indicated by\n"

