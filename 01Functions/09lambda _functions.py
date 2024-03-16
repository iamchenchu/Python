# Lambda Functions : A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression.

# Syntax : lambda arguments : expression

add = lambda x, y=1, z=1 : x + y + z
print(add(10)) # now for x it will consider the 10 value and for y and z it will take the default values.

print(add(123, 12))


# Lambda functions can take any number of arguments, but can only have one expression.

addition = lambda *args : sum(args) # can also take the unlimited number of arguments.
print(addition(1, 2, 3, 5, 8, 10, 14))
