import string

text = input(str("Введіть рядок: "))
cleaned = ""

for x in text:
    if x not in string.punctuation:
        cleaned += x

hashtag = "#" + cleaned.title().replace(" ", "")

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)
