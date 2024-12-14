# Functions and Variables

def print_one(arg1):
    print(f"arg1: {arg1}")

#print_one(1)
one = 1
print_one(one)

# Next program

def sum_function(*args):
    sum = 0
    for arg in args:
        sum += arg
    print(f"Sum: {sum}")

sum_function(33)
sum_function(20, 20, 20+4)
sum_function(20, 20, 20+4, 20-4)
sum_function(20, 20, 20+4, 20-4, 5*2)
sum_function(2/10, 10)
