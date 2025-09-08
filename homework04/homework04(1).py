list1 = [0, 1, 0, 12, 3, 0, 78, 20, 0, 'acb', 0, 195]
list2 = []

for i in list1:
    if i != 0:
        list2.append(i)

list3 = [0] * list1.count(0)
result = list2 + list3

print(result)
