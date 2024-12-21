# creating class

class MyClass:
    fruit = "Apple"

# creating object

f1 = MyClass
print(f1.fruit)

# __init__() function
# all classes in python have __init__() function
# __init__() is used to assign values to object properties

class Fruit:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

f1 = Fruit("Apple", "Brand_A")
print(f1)
print(f1.name)
print(f1.brand)

'''
<__main__.Fruit object at 0x0000025235AF6090>
Apple
Brand_A
'''

print("------------------------------------------------\n------------------------------------------------------------------")

# 2. __str__() 
# __str__() is used to define what the object will return

class Food_Item:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand
f3 = Food_Item("Rice", "Brand_B")
print(f3)
# returns >> <__main__.Fruit object at 0x000001AF05B664E0>

# solution

class Soap_Brand:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand
    def __str__(self):
        return(f"Name: {self.name}, Brand: {self.brand}")

soap_1 = Soap_Brand("Surf Excel", "ITC")
print(soap_1)

print("------------------------------------------------\n------------------------------------------------------------------")

# 3. object methods
# methods in objects are functions that belongs to that object

class Fan_Brand:
    def __init__(self, Brand, Type):
        self.Brand = Brand
        self.Type = Type
    
    def myFunc(self):
        print(f"Hey, I am a {self.Type} fan, manufactured by {self.Brand} ")

Fan = Fan_Brand("Havells", "Pedestal")
# print(Fan)
# returns nothing cause we have to call the function

print(Fan.myFunc())
# returns
'''
Hey, I am a Pedestal fan, manufactured by Havells 
None
'''
# directly call the function of the object
Fan.myFunc()
# Hey, I am a Pedestal fan, manufactured by Havells 

# another object

Fan1 = Fan_Brand("Usha", "Ceiling")
Fan1.myFunc()
# returns> Hey, I am a Usha fan, manufactured by Heleous 

print("------------------------------------------------\n------------------------------------------------------------------")

# 4. Self parameter
# used to access variables which belongs to the class
# it could be named anything but should be always first parameter of any function in the class

# example 1

class MySelfClass:
    def __init__(myself, name):
        print(f"My name is {name}")

name = MySelfClass("Ramlal")

# example 2

class YourselfClass:
    def __init__(yourself, name):
        yourself.name = name
        print(f"Your name is {name}")
yourname = YourselfClass("Rahul")
print(yourname)
# returns >> <__main__.YourselfClass object at 0x000001F26E8880B0>


print("------------------------------------------------\n------------------------------------------------------------------")

# 5.  modify object properties value
Fan1.Brand = "Crompton"
print(Fan1.Brand)
# result >> Crompton
# print(Fan1.Brand())
# TypeError: 'str' object is not callable

Fan1.myFunc()
# returns>> Hey, I am a Ceiling fan, manufactured by Crompton 

print("------------------------------------------------\n------------------------------------------------------------------")
# 6. __init__ and method both together

class ShirtClass:
    def __init__(self, brand):
        self.brand = brand
        print(f"Initialized object with name: {name}")
    
    def print_brand(self):
        print(f"My name is {self.brand}")

# create object (triggering __init__ )
obj = ShirtClass("Levis")

# call the method
obj.print_brand()
print("------------------------------------------------\n------------------------------------------------------------------")

# delete object properties
del Fan1.Brand
# print(Fan1.Brand)
#AttributeError: 'Fan_Brand' object has no attribute 'Brand'
print("------------------------------------------------\n------------------------------------------------------------------")

# delete object
del Fan1
#print(Fan1)
#NameError: name 'Fan1' is not defined.