# Recursion : A function calling itself is called recursion
# Recursion is a common mathematical and programming concept. It means that a function calls itself. 
# This has the benefit of meaning that you can loop through data to reach a result.
# The developer should be very careful with recursion as it can be quite easy to slip into writing a function
# which never terminates, or one that uses excess amounts of memory or processor power. However, when written
# Call Stack : calling the same function one after another is called call stack

# Recursive function
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
    print("END OF THE FUNCTION CALL")



show(5) # this will print the numbers from 10 to 1