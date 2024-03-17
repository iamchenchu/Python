name ="ChenchuReddy"

tar ='e'
for char in name:
    if char == tar:
        print(f"Found {tar} at index:", name.index(tar))

# using while loop
idx = 0
while idx < len(name):
    if name[idx] == tar:
        print(f"Found {tar} at index:", idx)
    else:
        print("finding....")
    idx += 1

