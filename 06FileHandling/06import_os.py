import os

file_path = os.path.join(os.getcwd(), "content.txt")
with open(file_path, "r") as file:
    print(file.read()) # reads the entire file

