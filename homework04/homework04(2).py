list1 = [0, 1, 7, 2, 4, 8]

if len(list1) >= 1:
    index = sum(list1[::2])
    result = index * list1[-1]
else:
    index = 0
    result = index

print(result)
