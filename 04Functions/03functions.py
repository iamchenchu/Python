def summing(*args):
    total = 0
    print(type(args)) 
    for n in args:
        total += n
    return total

print(summing(10, 20, 20)) # the arguments we pass here will be taken as a tuple and stored in args.
print(summing(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))