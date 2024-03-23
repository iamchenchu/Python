# we can read using multiple methods
# read() - reads the entire file
# readline() - reads a single line
# readlines() - reads all the lines and returns a list

with open("content.txt", "r") as file:
    print(file.read()) # reads the entire file

with open("content.txt", "r") as file:
    print(file.readline()) # reads the first line


file = open("content.txt", "r")
print(file.readlines()) # reads all the lines and returns a list
file.close() # close the file