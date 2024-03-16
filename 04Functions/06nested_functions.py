"""# Nested Functions: A function defined inside another function is called a nested function. Nested functions are able to access
 variables of the enclosing scope. In Python, these non-local variables are read-only by default and we must declare them 
 explicitly as non-local (using nonlocal keyword) in order to modify them.
  """

def calculator(*args):
    def calc_sum(*args):
        return sum(args)
    def calc_avg(*args):
        return sum(args)/len(args)
    def calc_prod(*args):
        prod = 1
        for i in args:
            prod *= i
        return prod
    
    return calc_sum(*args), calc_avg(*args), calc_prod(*args)

print(calculator(10, 20, 20))