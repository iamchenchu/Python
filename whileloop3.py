def table(number):
    x=1
    product=0
    while x<=10:
        product=x*number
        print(number,"*",x,"=",product)
        x=x+1
table(4)
print("----------------------")
table(10)