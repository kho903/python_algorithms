a, b = input().split()
a = list(a)
b = list(b)


def swap(word):
    temp = word[0]
    word[0] = word[2]
    word[2] = temp
    return word


a = "".join(swap(a))
b = "".join(swap(b))

print(a if a > b else b)
