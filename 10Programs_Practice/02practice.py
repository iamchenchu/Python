"""

"""

def max_customers():
    X = int(input("Enter a number of stoves : "))
    Y = int(input("Enter a total minutes : "))
    if X <= 0 or Y <= 0:
        return False, "Invalid input"
    else:
        print("The maximum number of customers that can be served is : ", X*Y)

max_customers()

# OR 

x,y = map(int, input().split())
ans = x*y
print(ans)