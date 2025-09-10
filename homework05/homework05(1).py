import string
import keyword
name = input("Введіть імʼя змінної: ")

if not name:
    print(False)
elif name[0].isdigit():
    print(False)
elif set(name) == {"_"}:
    print(len(name) == 1)
elif any(x.isupper() for x in name):
    print(False)
elif any(x.isspace() or (x in string.punctuation and x != "_") for x in name):
    print(False)
elif name in keyword.kwlist:
    print(False)
else:
    print(True)