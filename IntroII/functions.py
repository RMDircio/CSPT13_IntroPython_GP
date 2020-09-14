#----------------------------------------------------------------
''' Artem Litchanov's Lecture CSPT 8 '''

# define a doubling function that passes args by value
# simple variables get passed by value - ints, strings, bools
def double(x):
    return x * 2

print(double(12))

# define a doubling function for a list of variables passed by reference
# complex variables get passed by reference - functions, list, tuple, class, dictonary
def double_list(l):
    for index in range(len(l)):
        l[index] *= 2
    
y = double(12)
print(y)

number_list = [7,5,3]
print(number_list)
double_list(number_list)
print(number_list)
