#file Handling in python for text files
import os

file = input("Enter the name of file you want to open:")

if os.path.exists(file):
    filer = open(file, 'r')
    print(filer.read())
else:
    filew = open(file, 'w')
    filew.write("Hello!!! I created a new file for you")