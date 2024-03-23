with open('check.txt', 'r+') as file:
    file.write("I am from vermillion!\n")
    file.write("I am from vermillion!\n")
    file.write("I am from vermillion!\n")
    file.seek(0)
    content = file.read()
    print(content)

with open('check.txt', 'r+') as file:
    file.write("I am from vermillion!\n")
    file.write("I am from vermillion!\n")
    file.write("I am from vermillion!\n")
    file.seek(0)
    print(file.read())





