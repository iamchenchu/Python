for i in range(5):
    name = input("Enter a name :")
    file = open("names.txt", "a")
    file.write(f"{name} ") # It won't create name in new lines, instead it creates one by one without spaces so now we are adding space
    file.close()

# Try to run the files from the 06FileHandling to ignore the file creation out of the directory
# open() : is a function which is used for intialize the name of the file and mode of the file 
# write() : is a function which is used to write names to the file 
# close() : is a function which is used to close the file and save the changes
# "a" : append mode 
# "W" : it created the brand new file everytime we open the file 
# "r" : only reading the file