with open("names.txt", "r") as file:
    for _ in range(5):
        lines = file.readline()
        print(lines.rstrip())

