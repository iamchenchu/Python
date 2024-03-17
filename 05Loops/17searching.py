# Search for a tuple using the loop 

tuple1 = (1, 2, 4, 7, 9, 12, 8, 13, 1, 32, 4, 7, 9)

# using for loop
tar = 4
for i in tuple1:
    if tar == i:
        print(f"The Element {i} Fount at index:{tuple1.index(i)}")
    

# using while loop 
idx = 0
while idx < len(tuple1):
    if tar == tuple1[idx]:
        print(f"The Element {tar} Fount at index:{idx}")
    idx += 1
    