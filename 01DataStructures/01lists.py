# Lists 
"""
* Characteristics: Mutable, ordered collection of items.
* Creation: my_list = [1, 2, 3] or using the list() constructor.
* Common Operations:
    * Adding items: append(), extend(), insert()
    * Removing items: remove(), pop(), clear()
    * Other: sort(), reverse(), count(), index()
"""

# Creating a list
my_list = [1, 2, 3, 4, 5, 9, 7, 8, 6,0]
names = ["Chenchu", "Manohar", "Krishna", "Sai", "Srikanth"]
print(my_list)
print(names)
print(my_list[0])
print(names[-1])
print(my_list[1:3])
print(names[:3])
print(names[2:])
print(names[::2])

# Adding items
my_list.append(10)
print(my_list)
my_list.extend([11, 12, 13])
print(my_list)
my_list.insert(2, 20)
print(my_list)

# Removing items
my_list.remove(20)
print(my_list)
my_list.pop()
print(my_list)
my_list.clear()
print(my_list)

# Other operations
names.sort()
print(names)
names.reverse()
print(names)
print(names.count("Chenchu"))
print(names.index("Krishna"))
