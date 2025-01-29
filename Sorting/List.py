""" List Sorting """

print("====**** List Ascending Order ****====")

list1 = [10, 20, 4, 45, 99]
print('Sort list without method')
for i in range(len(list1)):
    for j in range(i + 1, len(list1)):
        if list1[i] >= list1[j]:
            list1[i], list1[j] = list1[j], list1[i]
print(list1)

print()
list2 = [10, 30, 4, 85, 79]
print('Sort list with function')
list2.sort()
print(list2)

print()

print("====**** List descending Order ****====")
print('Sort list without function')
l3 = [10, 20, 4, 45, 99]
for i in range(0, len(l3)):
    for j in range(i + 1, len(l3)):
        if l3[i] <= l3[j]:
            l3[i], l3[j] = l3[j], l3[i]
print(l3)
print()
print('Sort list with sort method')
l4 = [10, 20, 4, 45, 99]
l4.sort(reverse=True)
print(l4)
