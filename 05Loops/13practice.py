# Print numbers form 1 to 100 using for or range

for i in range(1, 101):
    print(i, end=' ')

print("\n")
print("\n")

# Print the nums from 100 to 1 

for i in range(100, 0, -1):
    print(i, end=' ')

print("\n")
print("\n")

# Print the multiplication of the n

n = int(input("Enter the number: "))
for i in range(1, 11, 1):
    print(n,"X",i,"=",n*i)
