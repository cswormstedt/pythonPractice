import sys


print('the command line arguments are:')

for i in sys.argv:
	print(i)

print('\n\n PYTHONPATH is', sys.path, '\n')