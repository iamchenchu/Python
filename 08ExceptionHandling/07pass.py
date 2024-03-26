
def main():
    a = get_int()
    print(a)

def get_int():
    while True:
        try:
            x = int(input("Enter a number:"))
        except ValueError:
            pass
        else:
            break
        return x