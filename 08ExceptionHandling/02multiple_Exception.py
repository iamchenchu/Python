
print("***************PROGRAM 1***************")
try:
    my_list = [1, 2, 3]
    print(my_list[3])

except (IndexError, ZeroDivisionError) as e:
    print("Index out of range or Cannot divide by zero")
    print(f"Exception: {e}")


print("***************PROGRAM 2***************")

try:
    print(10/0)
except (IndexError, ZeroDivisionError) as e:
    print("Index out of range or Cannot divide by zero")
    print(f"Exception: {e}")
