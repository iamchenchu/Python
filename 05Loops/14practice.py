# Write a program to find the sum of first n numbers

n = int(input("Please enter the number :"))
sum=0

for i in range(1, n+1):
    sum = sum + i

print("The sum of first", n, "numebers is ", sum)



# WAP to find the factorial of first n numbers (using for loop)

fact_num = int(input("Please enter the number to find the factorial:"))
fact = 1
for n in range(1, fact_num+1):
    fact *= n
    print("The factorial of", n, "is", fact)

