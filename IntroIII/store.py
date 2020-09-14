# lets write a store class with a name and categories

# class Store:
#     def __init__(self, name, categories):
#         # attributes
#         self.name = name
#         self.categories = categories

#     def __str__(self):
#         ret = f"{self.name}\n"
#         for i, c in enumerate(self.categories):
#             ret += "    " + str(i + 1) + ": " + c.name + "\n"
#         ret += "    " + str(i + 2) + ": Exit"
        
#         return ret

#     def __repr__(self):
#         return f"Store({self.name}, {self.categories})"

# how can we represent this class data as a string?

#----------------------------------------------------------------
''' Artem Litchanov's Lecture CSPT 8 '''

class Store:
    # attributes
    # name
    # categories - different departments

    # constructor - function that runs at every new instance
    # in python it is --> __init__()
    def __init__(self, name, categories): # self is the current instance of class
        # need to assign the variables
        self.name = name
        self.categories = categories
        self.employees = [] # make some employees

# make a function to share over all instances
# welcome message for example
    
    # __str__ --> cast instance of Class Store as a string for printing
    def __str__(self): 
        # return a string representing the store
        return f'Welcome to {self.name}! Here are some of our departments: {self.categories}'

# storesMONDAY_
print(sports_store)
print(grocery_store)

print(sports_store.name)
print(grocery_store.name)