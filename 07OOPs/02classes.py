class Demo:
    univ = "IIT"

    def __init__(self, n):
        print(self)
        print("Creating object")
        self.name = n
        print("Object created")

d1 = Demo("Chenchu")
d2 = Demo("Rajia")

print(d1.name)
print(d2.name)