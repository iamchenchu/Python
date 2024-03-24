try:
    x = int(input("Enter a number: "))
    if x < 0:
        raise ValueError("Sorry, no numbers below zero")
except ValueError:
    print("That's not a number")

else:
    print("No error Occured")