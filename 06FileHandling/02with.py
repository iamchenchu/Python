

for _ in range(5):
    name = input("Enter a name :")
    with open("names_file.txt", "a") as file:
        file.write(f"{name} ") # It won't create name in new lines, instead it creates one by one without spaces so now we are adding space

