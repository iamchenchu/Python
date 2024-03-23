# Tuple 
"""
* Characteristics: Immutable, ordered.
* Creation: my_tuple = (1, 2, 3) or using the tuple() constructor.
* Common Operations:
     * Accessing elements: via indexing my_tuple[0]
     * Counting: count()
     * Finding index: index()
     * Note: Cannot change elements due to immutability.
"""
# Creating a tuple
my_tuple = (1, 2, 3, 4, 5, 9, 7, 8, 6,0)
names = ("Chenchu", "Manohar", "Krishna", "Sai", "Srikanth")
print(my_tuple)
print(names)
print(my_tuple[0])
print(names[-1])
print(my_tuple[1:3])
print(names[:3])
print(names[2:])
print(names[::2])

# Counting elements
print(names.count("Chenchu"))
print(names.index("Krishna"))
# my_tuple[0] = 10  # This will raise an error
# my_tuple.append(10)  # This will raise an error
# my_tuple.remove(10)  # This will raise an error
# my_tuple.pop()  # This will raise an error
# my_tuple.clear()  # This will raise an error
# my_tuple.sort()  # This will raise an error
# my_tuple.reverse()  # This will raise an error
# my_tuple.insert(2, 20)  # This will raise an error
# my_tuple.extend([11, 12, 13])  # This will raise an error
# my_tuple.remove(20)  # This will raise an error

# Tuple unpacking
a, b, c = my_tuple[:3]
print(a, b, c)
# Tuple as keys in dictionary
my_dict = {
    (1, 2): "Tuple as key",
    (2, 3): "Another tuple as key"
}
print(my_dict[(1, 2)])
print(my_dict[(2, 3)])
# Tuple with one element
single_element_tuple = (1,)
print(single_element_tuple)
# Tuple without parentheses
tuple_without_parentheses = 1, 2, 3
print(tuple_without_parentheses)
# Tuple unpacking
a, b, c = tuple_without_parentheses
print(a, b, c)