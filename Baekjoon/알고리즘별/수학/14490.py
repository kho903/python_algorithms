def gcd(a, b):
    if b > a:
        a, b = b, a
    while b != 0:
        a %= b
        a, b = b, a
    return a


n, m = map(int, input().split(':'))
g = gcd(n, m)
print(f'{n//g}:{m//g}')
