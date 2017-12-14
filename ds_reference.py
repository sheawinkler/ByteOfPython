print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']

# mylist is just another name poitning to the same object
mylist = shoplist


del shoplist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
# both variables print the same list

print('Copy by making a full slice')

mylist = shoplist[:]

del mylist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)

print('The two lists are different')
