import os

# create a directory
os.mkdir("a_directory")

# change my current working directory
os.chdir("a_directory")

# list items on new directory
Files = os.listdir()

print("Files in newly created directory: ", Files)