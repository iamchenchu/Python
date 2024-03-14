import time
# Print the elements of the following list using a loop 
list1 = [1, 2, 4, 7, 9, 12, 8, 13, 1, 32, 4, 7, 9]
idx = 0

while idx < len(list1):
    print(list1[idx])
    time.sleep(1)  # Introduce a delay of 1 second
    idx += 1

print("End of the loop at ", idx)

idx1 = 0

names = ['John', 'Paul', 'George', 'Ringo', 'Brian', 'Stuart', 'Pete', 'Jimmy', 'John', 'George', 'Paul', 'Ringo']
while idx1 < len(names):
    print(names[idx1])
    time.sleep(1)  # Introduce a delay of 1 second
    idx1 += 1
