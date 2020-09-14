# # lets write a store class with a name and categories
# class Store:
#     def __init__(self, name, categories):
#         # attributes
#         self.name = name # string has_a name
#         self.categories = categories # has_a (has_many) composition

#     def __str__(self):
#         ret = f"{self.name}\n"
#         for i, c in enumerate(self.categories):
#             ret += "    " + str(i + 1) + ": " + c.name + "\n"
#         ret += "    " + str(i + 2) + ": Exit"
        
#         return ret

#     def __repr__(self):
#         return f"Store({self.name}, {self.categories})"

# # how can we represent this class data as a string?

#----------------------------------------------------------------#
#----------------------------------------------------------------#
#----------------------------------------------------------------#
''' Artem Litchanov's Lecture CSPT 8 '''

# import the category class we made
from category import Category
from store import Sneaker, SoccerBall


class Store:
    # attributes
    # name
    # categories - different departments


    # constructor (every class has one) - function that runs at every new instance
    # in python it is --> __init__()

    def __init__(self, name, categories): # self is the current instance of class
        # need to assign the variables
        self.name = name
        # example of composition here with categories
        self.categories = categories
        self.employees = [] # make some employees


# make a function to share over all instances
# welcome message for example
    
    # __str__ --> cast instance of Class Store as a string for printing
    def __str__(self):
        output = f'Welcome to {self.name}!'
        # loop over categories
        counter = 1
        for category in self.categories:
            output += f'\n {counter}. {category.name}'
            # increment the counter - adding it then setting it
            counter += 1
        
        # return a string representing the store
        return output


    # printing function - returns a string
    def __repr__(self):
        return f'Self.name = {self.name} ; self.categories = {self.categories}'


# items
virtue = SoccerBall('VBall',
                    '50',
                    'leather',
                    'Virtue Spots', 
                    'black and orange',
                    )

adidas = Sneakers('Adidas High Top',
                '100',
                '7',
                'ADIDAS STREET', 
                'High Top' 
                'White',
                'White',
                )

# new categories
# empty [] here is the product array - we are makeing it empty for now
running_category = Category('Running', "All your running needs", [adidas])
baseball_category = Category('Baseball', "Cubs Unite!", [])
basketball_category = Category('Basketball', 'Indoor and outdoor products', [])
football_category = Category('Football', 'The American kind', [])
soccer_category = Category('Soccer', 'The real football', [virtue])


### stores
sports_store = Store('REI', [running_category, baseball_category, baseball_category])

# put everything into a loop

choice = -1

print(sports_store)
print('Type q to quit')

while True:
    # READ
    choice = input('Please choose a category (#): ')
    try:    
        # EVALUATE
        if (choice =='q'):
            break
        choice = int(choice) -1
        if choice >= 0 and choice < len(sports_store.categories):
            chosen_category = sports_store.categories[choice]
            # PRINT
            print(chosen_category)
        else:
            print('The number is out of range')
        # how to prevent a error when strings are entered for choice
    except ValueError:
        print("Please enter a number")



