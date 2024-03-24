# Exception Handling
# Try : It is the block of code which is to be attempted
# Except : It is the block of code which is to be executed if there is an exception in the try block
# Else : It is the block of code which is executed if there is no exception in the try block
# Finally : It is the block of code which is executed irrespective of the exception in the try block
# Raise : It is used to raise an exception
# Assert : It is used to check if a condition is True, if not it will raise an exception
# Custom Exceptions : User defined exceptions
# Exception Hierarchy : BaseException -> Exception -> ArithmeticError -> ZeroDivisionError

values = [10, 20, 0, 30, 'Hello', 35, 40]

for value in values:
    try:
        # Tries to divide the value by 2, which may raise several types of exceptions
        print(value / 2)
    except ZeroDivisionError:
        # Handles division by zero, if 'value' is 0
        print("Cannot divide by zero")
    except TypeError:
        # Handles cases where 'value' is not a number, e.g., a string
        print("Cannot divide a string")
    except Exception as e:
        # Handles any other exceptions that are not caught by the above except blocks
        print(f"Exception: {e}")
    else:
        # Executes if the try block did not raise any exceptions
        print("No exception")
    finally:
        # Executes after try, except, and else blocks have executed, regardless of whether an exception was raised or not
        print("Finally block")
