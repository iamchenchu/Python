
# finally : The finally clause runs no matter what, often used for cleanup actions.

try:
    print(10/2)
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("No exception")
finally:
    print("Finally block")

print("********************")
try:
    print(10/0)
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("No exception")
finally:
    print("Finally block")