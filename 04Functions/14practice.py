def calc_avg(*args):
    sum = 0
    for i in range(len(args)):
        sum += args[i]
    print(f"The avg of the given arguments is: {sum/len(args)}")
    return sum/len(args)

print(calc_avg(10, 20, 20))     # this will print the avg the given arguments
calc_avg(10, 10, 20, 30)