
try:
    with open("no_file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")
    