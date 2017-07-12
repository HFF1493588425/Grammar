# print('hello world')

age = 20
name = 'john'
age2 = 30
name2 ='Mary'
print('{0} is {1} years old'.format(name,age))
# or the below example, but uglier
print( name + ' is ' + str(age) + ' years old')
print('{0} is bigger than 20'.format(age))
print('{1} is {0}'.format(name2,age2))
# output 30 is Mary
# {0},{1} represent the following arguments in the method, eg, name->0, age->1 or name2->1, age2->0

print('{0}'.format(1.0/3))
# decimal(.) precision of 3 for float o.333333333
print('{0:.3f}'.format(1.0/3))
# ^ put the text centered and takes 11 length with _ filled the space left
print('{0:_^11}'.format('hello'))

print('{name} wrote {book}'.format(name = 'swamp',book = 'a byte of python'))

print('a', end='')
print('b', end=' ')
print('c')

print('''ra rua rua rua a
ra ra la la rua a ru a
ra ra ra ra ru a ru a
''')

# raw string
print(r'new lines are indicated by \n')

i = \
5
# equals to
i = 5

# implicit line joining
first_4_month_of_year = {'Jan', 'Feb',
                         'Mar','Apr'}
jan = 'january'
feb = 'february'
print('examples of months', jan,feb)

