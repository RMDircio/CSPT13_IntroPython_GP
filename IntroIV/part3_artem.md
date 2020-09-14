#----------------------------------------------------------------
''' Artem Litchanov's Lecture CSPT 8 '''


 -----------                                 --------------
 -- Store --      ---- **"HAS a"** ---->     -- Category --
 -----------                                 --------------

        Store **has-a** category

# Composition / Association
- Store here is composed of one or many categories
- Category is associated with a store
- **HAS-A**
  
  
# Inheritance example for Sports Store
- **IS-A**
  
-------------------------
-- Class Product(self) --
-------------------------
These attributes are shared over all products
- Product has a name - an attribute
- Product has a price - an attribute
- Product has a sale precent - an attribute

products:
- Sneakers
- Soccer balls
- Weights
- Bicycles

## Not all the products listed will have the same attributes
We can inhertant a class in a new class that is made from special products

-------------                                ---------------
-- Sneaker --      ---- **"IS a"** ---->     --- Product ---
-------------                                ---------------

-----------------                             ---------------
-- Soccer Ball --    --- **"IS a"** --->      --- Product ---
-----------------                             ---------------


----------------------------
-- Class Sneaker(Product) --
----------------------------
This new class is inheriting all the attributes from the Product class:
- name
- price
- sale precent
  
New attributes to add to this new class
- Shoe size
- Brand
- Style
- Color

### Another class
----------------------------
-- Class Soccer_ball(Product) --
----------------------------
This new class is inheriting all the attributes from the Product class:
- name
- price
- sale precent
  
New attributes to add to this new class
- Brand
- Material
- Color