# Import argv list from the sys module
from sys import argv

script_name = argv[0]
argument1= argv[1]
argument2 = argv[2]

print("Script name: ", script_name)
print("Argument 1: ", argument1)
print("Argument 2: ", argument2)

'''
Run the script through cmd

python .\ex12.py Hello World

# It will return >>>>>>>

Script name:  .\ex12.py
Argument 1:  Hello
Argument 2:  World

'''