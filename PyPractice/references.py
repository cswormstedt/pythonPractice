print('Simple Assigment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
# myList is just another name pointing the same object
myList = shoplist


# I purchased the first item, so I remove
del shoplist[0]

print('shoplist is', shoplist)
print('myList is', myList)
# this confirms that they point to the same object

print('copy by makin full slice')
# make a copy by doing a full slice
myList = shoplist[:]
# remove first item
del myList[0]

print('shoplist is', shoplist)
print('myList is', myList)
# now the lists are different
