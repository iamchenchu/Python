# Break :  To stop the loop even if the condition is true
# Continue : Terminates the current iteration and continues with the next iteration

i = 0

while i <= 5:
    if(i==3):
        i+=1  # If we don't increment the value of i, it will be an infinite loop
        continue    # It will skip the current iteration and continue with the next iteration
    print(i)
    i+=1

