# Write program to calculate and print the first n natural numbers sum using recursion.


def sum_natural(n):
    if n == 0:
        return 0
    return sum_natural(n-1) + n

print(sum_natural(5))