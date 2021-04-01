def prime_list(n):
    a = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if a[i]:
            for j in range(i + i, n, i):
                a[j] = False
    return [i for i in range(2, n) if a[i] == True]


while True:
    n = int(input())
    if n == 0:
        break
    prime_res = prime_list(2 * n + 1)
    print(len([i for i in prime_res if i > n]))
