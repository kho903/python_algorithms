def gcd(a, b):
    if b > a:
        a, b = b, a
    while b != 0:
        a %= b
        a, b = b, a
    return a


x, y = map(int, input().split())
print(x + y - gcd(x, y))
