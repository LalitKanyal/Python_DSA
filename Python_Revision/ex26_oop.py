class Person(object):

    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession

    def talk(self, words):
        print(f"I am {self.name} and {words}")

# print(Person("Lalit", 96, "IT Engineer"))
# <__main__.Person object at 0x0000023DC44A6180>

lalit = Person("Lalit", 96, "IT Engineer")
#find dict inside object and class using __dict__
# print(lalit.__dict__)
lalit.talk("I am coding")


# class that lalit comes
print(lalit.__class__)
# <class '__main__.Person'>

# contents of the class
print(lalit.__class__.__dict__)
# {'__module__': '__main__', '__init__': <function Person.__init__ at 0x00000239FA3D8FE0>, 'talk': <function Person.talk at 0x00000239FA3D9120>, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}

# show attributes of object
print(dir(lalit))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'name', 'profession', 'talk']


