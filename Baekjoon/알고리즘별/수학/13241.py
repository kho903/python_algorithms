def gcd(a, b):
    if b > a:
        a, b = b, a
    while b != 0:
        a %= b
        a, b = b, a
    return a


a, b = map(int, input().split())

print(a * b // gcd(a, b))
