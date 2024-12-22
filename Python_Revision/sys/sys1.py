# sys module in python
# The sys module in Python provides functions and variables that interact with the Python runtime environment.

# print command line arguments
import sys
print("Arguments passed to script:", sys.argv)

# run the script 
#python .\sys1.py argument1, argument 2

# returns
# Arguments passed to script: ['.\\sys1.py', 'argument1', 'argument', '2']'''

# version of python
print("Python version:", sys.version)
# Python version: 3.12.7 | packaged by Anaconda, Inc. | (main, Oct  4 2024, 13:17:27) [MSC v.1929 64 bit (AMD64)]

# python platform
print("Running on platform:", sys.platform)
# returns
# Running on platform: win32

# Exit the script
print("Exiting the script")
sys.exit(0)
# 0 means successful termination
