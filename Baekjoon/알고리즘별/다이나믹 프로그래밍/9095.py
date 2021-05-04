t = int(input())


def p123(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        return p123(num - 3) + p123(num - 2) + p123(num - 1)


for _ in range(t):
    n = int(input())
    print(p123(n))
