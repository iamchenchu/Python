# Dictionary 
"""
* Characteristics: Mutable, unordered (ordered as of Python 3.7), key-value pairs.
* Creation: my_dict = {'key': 'value'} or using the dict() constructor.
* Common Operations:
     * Adding/updating items: my_dict['key'] = 'value'
     * Removing items: pop(), popitem(), clear()
     * Accessing: keys(), values(), items()
"""

# Creating a dictionary
my_dict = {
    "name": "Chenchu",
    "age": 25,
    "city": "Hyderabad"
}
print(my_dict)
print(my_dict["name"])
print(my_dict.get("age"))
print(my_dict.get("city"))
print(my_dict.get("country"))
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
