
b = 1

while b <= 20:
    if b == 13:
        print("Number is 13 so I am stopping the loop")
        break
    elif b == 10:
        print("Number is 10 so I am skipping the iteration")
        b += 1
        continue
    print("Iteration is :", b)
    b += 1
