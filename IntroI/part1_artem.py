#----------------------------------------------------------------
''' Artem Litchanov's Lecture CSPT 8 '''

# $$$-------------------- $$$
### PRINTING ###

# declare a variable
name = 'Han Solo'

# print variable
print(name)

# string concatenation
print('Good day ' + name)

# ${name}
print(f'Well Met {name}')

# $$$-------------------- $$$
### DATA STRUCTURES ###

# List (not called array)
p = [10, 12, 13, 'Han', 14]
print(p)

# add an element to the end of p
p.append(777)
print(p)

# loop over list p and print each element
# for every element in p, so some sort of code
for element in p:
    print(element)

# print the index and element at the each index of p
for (index, enumerate) in enumerate(p):
    print(f'Element at {index} is {p[index]}')

# $$$-------------------- $$$
### LIST COMPREHENSIONS ###

# another way to create a list
number_list = [1, 4, 9, 16, 25]

# create a new list, of squares from the numbers list
squares = []
for number in number_list:
    squares.append(number*number)
    print('New Loop')
    print(squares)
print(squares)

# do the same above but on one line = list comprehension!
# [FUNCTION(VARIABLE) for VARIABLE in SOME_LIST]
better_squares = [number**2 for number in number_list]

# create a list of just even numbers
# % 2 == 0 means divide by 2 and no remainders
evens = [number for number in number_list if number % 2 == 0]
print('Even numbers',evens)

# create a new list with only name that start with 's'
names_list = ['Sara', 'jorge', 'Tammie', 'Mike', 'David']

s_names = [name.capitalize() for name in names_list if name[0].lower() == 's']
print(s_names)

# another way to look at the code above
s_names_verbose = []
for name in names_list:
    if(name[0].lower() == 's'):
        s_names_verbose.append(name.capitalize())

# $$$-------------------- $$$
### DICTIONARIES ###
# key --> value data structure

new_dict = {}

food_dict = {
    'apple' : 'is a fruit',
    'carrot': 'is a vegetable'
}

print(food_dict)

# add a new key : value pair
food_dict['cucumber'] = 'is a fruit now'
print(food_dict)

# access and print a certain element in food_dict
chosen_food = 'apple'
print(food_dict[chosen_food])

# iterate through the key : values in dictonary
# for elemnet in dict, do some code

for key, value in food_dict.items():
    print(f'{key} : {value}')

# check if an element exists in dictonary
print('apple' in food_dict)
print('pear' in food_dict)

# $$$-------------------- $$$
### TUPLES AND SETS ###

# tuple example
# can not be changed
tup = (1, 2, 3)

# can iternate tuples
for item in tup:
    print(item)

# access tup at index
print(tup[2])

# set example
# set = dictonaries without values & have no order
fruit = {'cucumber', 'apple', 'orange'}

for item in fruit:
    print(item)

if 'cucumber' in fruit:
    print("Time to make a salad!")

