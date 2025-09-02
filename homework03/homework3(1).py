a = int(input('Введіть перше число: '))
b = int(input('Введіть друге число: '))
c = input('Яку дію ви бажаєте виконати?(+, -, *, /): ')

if c == '+':
    print(a,"+",b, "=", a + b)
elif c == '-':
    print(a,"-",b, "=", a - b)
elif c == '*':
    print(a,"*",b, "=", a * b)
elif c == '/':
    if b == 0:
        print("На нуль ділити не можна!")
    else:
        print(a,"/",b, "=", a / b)
else:
    print("Введіть тільки допустимі значення")