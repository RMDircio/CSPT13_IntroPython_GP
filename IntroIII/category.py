# lets create a class to hold our category data

# class Category:
#     def __init__(self, name):  #, products):
#         self.name = name
#         # self.products = products

#     def __str__(self):
#         return f"No Products in {self.name}"


#----------------------------------------------------------------#
#----------------------------------------------------------------#
#----------------------------------------------------------------#

''' Artem Litchanov's Lecture CSPT 8 '''

class Category:
    # everytime you make a new class - define __init__
    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

    def __str__(self):
        return f'{self.name}: {self.description}'