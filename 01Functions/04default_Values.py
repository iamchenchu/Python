# Default values in function(): the default value is used when the function is called without a value for the parameter.

def calc_sum(a=10, b=20):
    return a + b

print(calc_sum()) # now it will take the default parameters as parameters.

print(calc_sum(100, 200)) # now it will take the passed parameters as parameters.

print(calc_sum(100)) # now it will take the passed parameter as a and default parameter as b.