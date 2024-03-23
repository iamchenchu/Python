with open('content.txt', 'r') as file:
    print(file.read())


with open('content.txt', 'r') as file1:
    print(file1.readline())

with open('content.txt', 'r') as file3:
    print(file3.readlines())

file3 = open('content.txt', 'r')
print(file3.readlines())
file3.close()