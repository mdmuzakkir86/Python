dic = {"name": "Muzakkir", "age": 23, "gender": "Male"}
print(dic)

for key in dic:
    print(key, ':', dic[key])

person = dict({'Id': 101, 'Name': 'Muzakkir', 'Gender': 'Male'})
for key_value in person.items():
    print(key_value[0], ':', key_value[1])

print(len(person), '\n\n')

person['age'] = 23
person.update({'height': 10, 'Charecter': 'Good'})
print(person)

person.setdefault('Phone', 9765657672)
person.setdefault('Location', "MBNR")

person['age'] = 25
person.update({'Phone': 1123345667})

# deleted_items = person.pop('location')


for key in person:
    print(key, ':', person[key])
