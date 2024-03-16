# Practice Questions
# 2. Search for a number in the below tuple and print the index of the number:


tuple1 = (10, 20, 30, 40, 50, 100, 200, 300, 20, 500, 20)

for i in range(len(tuple1)):
    if tuple1[i] == 20:
        print("the number 10 found at the index of ",i, " In the tuple")
    else:
        print(tuple1[i])
