age = int(input("Please enter your age :"))

if age >= 18:
    print('You are an adult')
if age < 18:
    print('You are a child')
if age <= 14:
    print('You are a kid')
else: 
    print('You are a grown up man')

#The above code is not efficient, we can use elif to make it more efficient because it will stop checking the conditions once it finds the first true condition
#The if is not efficient because it checks all the conditions even if the first condition is true