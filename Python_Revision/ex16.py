# Dictionaries and Functions


# Function Names are variables
# Functions can be assigned to variables and called using those variables.


def print_number(x):
    print("Number is: ", x)
print_number(100)
rename_print = print_number
rename_print(100)
#rename_print(200)


# confirming that they are pointing to the same function object.
print(id(print_number))
print(id(rename_print))

# 2. Dictionaries with Variables

color = "Green"

mahindra = {
    "color": color
}

print("SUV", mahindra["color"], "Mahindra")

# 3. Dictionaries with Functions

def run():
    print("Vroom")

tata = {
    "color": "RED",
    "run": run
}

print("My", tata["color"], "can go")
tata["run"]()