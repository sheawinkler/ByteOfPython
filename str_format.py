age = 20
name = 'Swaroop'

print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))

# decimal precision of 3 for float '0.333'
print('{0:.3f}'.format(1.0/3))
#fill with underscores with the text centered
print('{0:_^11}'.format('hello'))
#keyword-based formatting
print('{name} wrote {book}'.format(name='Swaroop', book='A byte of Python'))

#print always ends with \n
#to prevent new line use empty single quotes or add spaces/characters between quotes
print('a', end='')
print('b', end='')
