t = int(input())


def padoban(n):
    if n == 1 or n == 2 or n == 3:
        return 1
    elif n == 4 or n == 5:
        return 2
    else:
        lst = [1, 1, 1, 2, 2]
        i = 5
        while i < n:
            lst.append(lst[i - 3] + lst[i - 2])
            i += 1
    return lst[-1]


for _ in range(t):
    n = int(input())
    print(padoban(n))
