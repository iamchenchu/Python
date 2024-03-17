# Print the elements o the following list using a loop
# list1 = [1, 2, 4, 7, 9, 12, 8, 13, 1, 32, 4, 7, 9]

list1 = [1, 2, 4, 7, 9, 12, 8, 13, 1, 32, 4, 7, 9]

# using for loop
for i in list1:
    print(i, end=' ')

print()

# using while loop
idx = 0
while idx <len(list1):
    print(list1[idx], end=' ')
    idx += 1
print()

