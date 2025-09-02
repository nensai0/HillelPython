# a = 0
#
# if a < 0:
#     print("a is negative")
#     if a < -100:
#         a = a + 20
#         print('a < -100')
#     a = -a
# else:
#     print("a is non-negative")
#     if a > 100:
#         a = a - 20
#         print('a > 100')
#     else:
#         a = a + 40
#
# print("a:", a)

# ------------------

# a = 0
#
# if a < 0:
#     print('a is negative')
# elif a < -100:
#     a = a + 20
#     print('a < -100')
# elif a > 100:
#     a = a -20
#     print('a > 100')
# elif a == 0:
#     print('a is 0')
# else:
#     print('a is non-negative')
#     a = a + 40
#
# print('a:', a)

# ---------------------

# age = int(input('Enter your age: '))
#
# if age < 0:
#     print('Age cannot be negative')
# elif age > 0 and age < 10:
#     print('Drink mil')
# elif age > 10 and age < 20:
#     print('Drink juice')
# elif age >= 21 and age < 100:
#     print('Drink whisky')
# else:
#     print('Drink nothing')

# ------------------------

a = 0

if a < 0:
    res = 'negative'
else:
    res = 'non-negative'
print('res: ', res)

res_2 = 'negative' if a < 0 else ('zero' if a == 0 else 'non-negative')
print('res_2: ', res_2)
