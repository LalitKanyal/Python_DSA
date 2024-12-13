# create a function

def a_function():
    print('This is a function')

# call a function
a_function()

# Arguments (also called args)

def b_function(color):
    print(color + " fish")

b_function("red")
b_function("yellow")
b_function("blue")


# multiple arguments

def c_function(name, mail, address):
    print("Employee details are: " + name + " " + mail + " " + address)

c_function("Miguel", "mailtomiguel@gmail.com", "New Mexico")
c_function("Durov", "mailtodurov@gmail.com", "France")
c_function("Alexendar", "mailtoalex@gmail.com", "USA")

# Arbitrary Arguments, *args
# when we do not know how many arguments that will be passed in our function, we add * before the parameter name

def color_names(*colors):
    print("My favorite color is: " + colors[1])

color_names("Red", "Yellow", "Blue")

# Keyword Arguments
# sending arguments in key value syntax

def planets(planet1, planet2, planet3):
    print("The nearest planet to Sun is: " + planet1)

planets(planet1="Mercury", planet2="Venus", planet3="Earth")

# Arbitrary Keyword Arguments
# **kwargs

def planets1(**planet):
    print("The nearest planet to Sun is: " + planet[0])

planets(planet1="Mercury", planet2="Venus", planet3="Earth")


# Passing list as an argument

def a_func(colors):
    for color in colors:
        print (color)

colors = ["red", "green", "blue"]

a_func(colors)