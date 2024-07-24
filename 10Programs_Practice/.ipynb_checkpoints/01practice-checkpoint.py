
# Prime number 

def is_prime(n):
    if n<=1:
        return False, f"{n} is not a prime number because it is less than 1"
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False, f"{n} is not a prime number because it is divisible by {i}"
        return True, f"{n} is a prime number"
    
print(is_prime(10))
print(is_prime(101))
print(is_prime(13))
print(is_prime(7))

