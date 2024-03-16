def function_with_both(*args, **kwargs):
    for arg in args:
        print(arg)
    
    for kwarg in kwargs:
        print(kwarg, ":", kwargs[kwarg])

function_with_both(1, 2, 3, 4, 5, name='John', age=25, city='New York') # This will print the tuple of positional arguments and the dictionary of keyword arguments.