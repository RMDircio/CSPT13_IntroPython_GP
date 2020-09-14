# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def __str__(self):
#         return f"{self.name}    ${self.price}"


#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------
''' Artem Litchanov's Lecture CSPT 8 '''

# this is the PARENT/BASE/SUPER CLASS
# always the smaller class
class Product:
    def __init__(self, name, price, discount = 0):
        self.name = name
        self.price = price
        # this attribute is NOT added manualy to others below
        # this was added after new classes were made
        # still inherited to child classes
        self.discount = 0

    # a printing function
    def __str__(self):
        return f'{self.name}: ${self.price} - this is a great deal!'

# adding random item to product class
generic_product = Product('Value_U', '0.99')
print(generic_product)


# this is a CHILD/SUB CLASS
# always the larger class
class Sneakers(Product):
    # add new params here after orginals from Product class
    def __init__(self,
                name, 
                price, 
                shoe_size, 
                brand, 
                style, 
                color,
                ):
        # get params from Product class 
        # this is the Parent Class Instance
        super().__init__(name, price)
        
        # set new params here
        self.shoe_size = shoe_size
        self.brand = brand
        self.style = style
        self.color = color

# sneaker test

# (name, price, shoe_size, brand, style, color)
adidas = Sneakers('Adidas High Top',
                '100',
                '7',
                'ADIDAS STREET', 
                'High Top' 
                'White',
                'White',
                )

print(adidas.name)
print(adidas.price)
print(adidas.color)
print(adidas)

# this is another CHILD/SUB CLASS
# always the larger class
# soccer ball test
class SoccerBall(Product):
    # add new params here after orginals from Product class
    def __init__(self,
                name, 
                price, 
                material, 
                brand, 
                color,
                ):
        # get params from Product class 
        # this is the Parent Class Instance
        super().__init__(name, price)
        
        # set new params here
        self.material = material
        self.brand = brand
        self.color = color

    # overwrite the __str__ function to make a new message
    def __str__(self):
        # still keep the parent __str__
        parent_str = super().__str__()
        return f'{parent_str} travels farther!'

    # new function
    def kick(self):
        print('ANNNND Team Rocket Flies Off Again!')

# (name, price, material, brand, color)
virtue = SoccerBall('VBall',
                    '50',
                    'leather',
                    'Virtue Spots', 
                    'black and orange',
                    )

print(virtue.name)
print(virtue.price)
print(virtue.color)
print(virtue.color)
print(virtue)
print(virtue.kick())



