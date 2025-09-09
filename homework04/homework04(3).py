import random
list1 = []
a = random.randint(3, 10)

for _ in range(a):
    list1.append(random.randint(1, 100))

print("Початковий список:", list1)
print("Новий список:", [list1[0], list1[2], list1[-2]])
