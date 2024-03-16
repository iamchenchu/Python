# Decorators : A decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.

# syntax : def decorator_function(func):

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_hello():
    print("Hello!")

decorated_hello = my_decorator(say_hello)
decorated_hello()

# In this example : my_decorator is a decorator function. It takes say_hello function as an argument and extends its behavior.
# The wrapper function is the decorator function. It takes say_hello function as an argument and extends its behavior.

@my_decorator
def say_goodbye():
    print("Goodbye!")

say_goodbye() # This is equivalent to say_goodbye = my_decorator(say_goodbye), but more readable and commonly used.

# In this example : @my_decorator is a decorator. It takes say_goodbye function as an argument and extends its behavior.
