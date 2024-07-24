# Else clause : no exception in the try block

try:
    print(10/2)
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("No exception")

print("********************")
try:
    print(10/0)
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("No exception")