def calc_avg(*args):
    sum = 0
    for i in args:
        sum +=i
    return sum/len(args)
print(calc_avg(10, 20, 20))          # this will print the avg the given arguments 
print(calc_avg(10, 10, 20, 30))      # this will print the avg the given arguments
