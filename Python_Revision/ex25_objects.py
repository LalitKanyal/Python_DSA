# 1. Passing dictionary to a function

# Shop_owner = {
#     "name": "Chote lal",
#     "age" : 44,
#     "shop type": "Food Stall"
# }

# def talk(name, words):
#     print(f"My name is {name['name']} and {words}")

# talk(Shop_owner, "I am talking.")


# Talk inside the dict
# 2. 

def talk(who, words):
    print(f"My name is {who['name']} and {words}")
    
Shop_owner = {
    "name": "Chote lal",
    "age" : 44,
    "shop type": "Food Stall",
    "talk": talk
}

Shop_owner['talk'](Shop_owner, "Hi, I am here")


# 3. Closures

# A closure is any function that’s created inside another
# function but accesses data in its parent


# this function makes functions
def constructor(color, size):
    print(">>> constructor color:", color, "size:", size)

    def repeater():
        print(">>> repeater color:", color, "size:", size)
    
    print("<<< exit constructor")
    return repeater

blue_xl = constructor("blue", "xl")
green_sm = constructor("green", "sm")

for i in range(0,4):
    blue_xl()
    green_sm()

# -------------------------------

def outer_func():
    name = "Pythonista"
    def inner_func():
        print(f"Hello, {name}!")
    inner_func()


outer_func()


greeter = outer_func()
print(greeter)