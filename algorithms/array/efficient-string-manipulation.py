document = "My name is jaison and we are removing all non alphabets from this string"


def inefficient():
    letters = ''
    for c in document:
        if c.isalpha():
            letters += c
    print(letters)


def efficient():
    temp = []
    letters = ''
    for c in document:
        if c.isalpha():
            temp.append(c)
    letters = ''.join(temp)
    print(letters)


efficient()
