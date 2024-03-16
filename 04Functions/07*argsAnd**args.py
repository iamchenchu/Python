"""
*args: *args is used to pass a variable number of non-keyworded arguments list and the function takes them as a tuple.
**kwargs: **kwargs is used to pass a variable number of keyworded arguments dictionary to a function.
"""

def function_with_both(*args, **kargs):
    print(args)  # This will print the tuple of positional arguments.
    print(kargs)  # This will print the dictionary of keyword arguments.
    print(type(args))  # This prints the type of args (<class 'tuple'>).
    print(type(kargs))  # This prints the type of kargs (<class 'dict'>).

function_with_both(1, 2, 3, 4, 5, name='John', age=25, city='New York')
