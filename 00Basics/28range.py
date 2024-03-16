# range() : It is a built-in function in Python that generates the integer numbers between the given start integer to 
# the stop integer. It is a part of the Python Built-in Functions. The range() function is used to generate a sequence of numbers.
# It is often used with the for loop to iterate over a sequence of numbers.

# Syntax: range(start, stop, step)
# start: Optional. An integer number specifying at which position to start. Default is 0

for i in range(5):
    print("Hello world it is iteration ", i)

print("***********************")

for i in range(5, 10):
    print("Hello world it is iteration ", i)

print("***********************")

for i in range(1, 10, 2):
    print("Hello world it is iteration ", i)