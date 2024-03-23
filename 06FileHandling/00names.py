names = []

for _ in range(5):
    name = input(f"Enter a name{_} :")
    names.append(name)

print(names)

names =sorted(names)
for name in names:
    print(f"Hello {name}")

print(names)

""" 'r' - Read mode (default)
    'w' - Write mode, creates a new file or truncates the existing file
    'a' - Append mode, for adding new content to the end of the file
    'b' - Binary mode for binary files (used with other modes, e.g., 'rb', 'wb')
    '+' - Update mode, for reading and writing to the same file (e.g., 'r+', 'w+')"""