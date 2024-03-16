
i =1

while i < 10 :
    if i % 2 == 0:
        i += 1
        continue   # It will skip the current iteration and continue with the next iteration
    print("Hello world it is iteration ", i)
    i += 1