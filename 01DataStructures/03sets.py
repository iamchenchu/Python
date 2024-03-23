# Sets
"""
* Characteristics: Mutable, unordered, unique elements.
* Creation: my_set = {1, 2, 3} or using the set() constructor.
* Common Operations:
     * Adding items: add()
     * Removing items: remove(), discard(), pop(), clear()
     * Set operations: union(), intersection(), difference(), symmetric_difference()
"""

# Creating a set
my_set = {1, 2, 3, 4, 5, 9, 7, 8, 6,0}
names = {"Chenchu", "Manohar", "Krishna", "Sai", "Srikanth"}
print(my_set)
print(names)

# Adding items
my_set.add(10)
my_set.add(11)
my_set.add(1)
print(my_set)

# Removing items
my_set.remove(7)
print(my_set)
my_set.discard(10)
print(my_set)
my_set.pop()
print(my_set)
my_set.clear()

# Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))

