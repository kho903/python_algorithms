def prime_list(n):
    a = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if a[i]:
            for j in range(i + i, n, i):
                a[j] = False
    return [i for i in range(2, n) if a[i] == True]


n = int(input())
for _ in range(n):
    num = int(input())
    p_l = prime_list(num)
    d = int(num / 2)
    while True:
        if d in p_l:
            if num - d in p_l:
                print(d, num - d)
                break
        d -= 1
