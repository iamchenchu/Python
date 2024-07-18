
# filter(): This function filters the elements of an iterable based on a function.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

even_numbers = list(filter(lambda x : x % 2 == 0, numbers)) 
print(even_numbers)
