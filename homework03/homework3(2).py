list1 = [12, 34, 56, 78, 'abc']

if len(list1) <= 1:
    result = list1
else:
    result = [list1[-1]] + list1[:-1]

print(result)