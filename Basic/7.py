'''
7. File Extension Extractor

Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java
'''

filename = input("Enter a file with extension:")
splitter = filename.split(".")[1]
print(f"The File extension is .{splitter}")