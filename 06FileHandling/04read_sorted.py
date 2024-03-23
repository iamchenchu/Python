names = []
with open("names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip()) # rstrip() Removes the white spaces and lines

for name in sorted(names):
    print(f"Hello {name}")