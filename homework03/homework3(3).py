# list1 = [1, 2, 3,]
#
# if len(list1) % 2 == 0:
#     mid = len(list1) // 2
#     result1 = [list1[:mid]] + [list1[mid:]]
# elif len(list1) == 0:
#     mid = len(list1) // 2
#     result1 = [list1[:mid]] + [list1[mid:]]
# else:
#     mid = len(list1) // 2 + 1
#     result1 = [list1[:mid]] + [list1[mid:]]
#
# print(result1)

list1 = [1, 2, 3, 4, 5]

if len(list1) % 2 == 0:
    mid = len(list1) // 2
else:
    mid = len(list1) // 2 + 1

result = [list1[:mid], list1[mid:]]
print(result)
