# empty function

def do_nothing():
    pass

# call function
do_nothing()

# normal function
def do_something():
    print("Hello!")

# call function
do_something()

# Function Arguments

def addition(a, b):
    print(a+b)

addition(2,3)

# *args
def addition_one(*args):
    print("Arguments:", args)
    total = sum(args)
    print("Sum of all arguments: ", total)

addition_one(1,2,3,4)

# loop in arg

def addition_two(*args):
    print("Arguments: ", args)
    total = 0
    for arg in args:
        total += arg
    print("Sum of all args: ", total)

addition_two(1,2,3,4,5)

# Multiply each argument with 2

def multiplication(*args):
    print("Multiple Arguments ", args)
    result = []
    for arg in args:
        result.append(arg*2)
    print(result)

multiplication(1,2,3,4,5)