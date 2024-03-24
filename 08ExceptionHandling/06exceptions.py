
def main():
    a = get_int()
    print(a)


def get_int():
    while True:
        try:
            x = int(input("Enter a number:"))
        except ValueError:
            print("That's not a number")
        else:
            break
        return x

main()