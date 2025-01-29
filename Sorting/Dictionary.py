# Sorting dictionary using inbuilt method
print("====**** Dictionary Ascending Order ****====")

# returning only keys
dict1 = {'Ten': 10, 'One': 1, 'Two': 2, 'Seven': 7}
print("KEY BASED SORTING | Only keys")
print(sorted(dict1.keys()))
print()

# Returning only values
print("VALUE BASED SORTING | Only Values")
print(sorted(dict1.values()))
print()

# Returning both key and value
print("VALUE BASED SORTING")
sorted_dict1 = {key: value for key, value in sorted(dict1.items(), key=lambda item: item[1])}
print(sorted_dict1)
print()

# Returning both key and value
print("KEY BASED SORTING")
sorted_dict2 = {key: value for key, value in sorted(dict1.items(), key=lambda key: key[0])}
print(sorted_dict2)
print()

# Sorting dictionary without inbuilt method
print('VALUE BASED SORTING WITHOUT INBUILT FUNCTIONS')
sorted_values = sorted(dict1.values())
sorted_dict = {}
for i in sorted_values:
    for k in sorted(dict1.keys()):
        if dict1[k] == i:
            sorted_dict[k] = dict1[k]
            break

print(sorted_dict)
print()

print('KEY BASED SORTING WITHOUT INBUILT FUNCTIONS')
