# Search a number in the below tuple 
tuple1 = (1, 2, 4, 7, 9, 12, 8, 13, 1, 32, 4, 7, 9, 13)

i = 0
while i < len(tuple1):
    if tuple1[i] == 13:
        print("Number 13 found at index ", i)
    else:
        print("Finding 13...")
    i += 1