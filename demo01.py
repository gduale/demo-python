#!/usr/bin/env python3

# Creating a dictionary
my_dictionary = dict()
my_dictionary2 = {}

# Displaying the type for verification
print(type(my_dictionary))
print(type(my_dictionary2))

# Filling the dictionary (key: value)
my_dictionary = {"Car": "Yaris", "Engine": "4ch", "Doors": 5}
print(my_dictionary)

# Adding an entry to the dictionary
my_dictionary["Seats"] = 5
print(my_dictionary)

# Displaying a key's value
print(my_dictionary["Engine"])

# Deleting an entry from the dictionary
del my_dictionary["Doors"]
print(my_dictionary)

# Looping through dictionary keys
for key in my_dictionary.keys():
    print(key)

# Looping through dictionary values
for value in my_dictionary.values():
    print(value)

# Looping through a dictionary (keys and values)
for key, value in my_dictionary.items():
    print(key, value)

# Creating a list
my_list = list()
my_list2 = []

# Displaying the type for verification
print(type(my_list))
print(type(my_list2))

# Filling the list
my_list = [1, 2, 3, "Blue"]
print(my_list)

# Adding an entry to the list
my_list.append(4)
print(my_list)
my_list.append("Purple")
print(my_list)

# Removing an entry from the list
del my_list[0]
print(my_list)
my_list.remove("Blue")
print(my_list)

# Displaying an element of the list, here '3' is an index, it will display "Blue".
print(my_list[3])

# Looping through a list
for element in my_list:
    print(element)

# Looping with consideration of the index
for index, element in enumerate(my_list):
    print(index, element)
