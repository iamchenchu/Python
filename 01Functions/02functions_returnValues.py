# calc_sum(*args) : We can pass unlimited number of arguments to a function using *args.
# *args : *args is used to pass a variable number of non-keyworded arguments list and the function takes them as a tuple.

# return : The return statement is used to exit a function and go back to the place from where it was called.

def calc_sum(*args):
    return sum(args)

print(calc_sum(10, 20, 20))
print(calc_sum(10, 10, 20))
print(calc_sum(10, 1, 10, 4, 5))
print(calc_sum(1, 1, 10, 4, 5, 1))