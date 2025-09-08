list1 = [12, 34, 56, 78, 'abc']

if len(list1) <= 1:
    result = list1
elif len(list1) == 1:
    result = list1
else:
    last_element = list1[-1]
    element1 = list1[:-1]
    result = [last_element] + element1

print(result)