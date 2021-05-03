def gcd(a, b):
    if b > a:
        a, b = b, a
    while b != 0:
        a %= b
        a, b = b, a
    return a


n = int(input())
r = list(map(int, input().split()))
f = r[0]
for i in range(1, n):
    g = gcd(f, r[i])
    print(f'{f // g}/{r[i] // g}')
