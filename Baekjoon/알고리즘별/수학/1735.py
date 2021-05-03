def gcd(a, b):
    if b > a:
        a, b = b, a
    while b != 0:
        a %= b
        a, b = b, a
    return a


n = []
m = []
for _ in range(2):
    a, b = map(int, input().split())
    n.append(a)
    m.append(b)
g = gcd(m[0], m[1])

u = n[0] * m[1] // g + n[1] * m[0] // g
d = m[0] * m[1] // g
if gcd(u, d) == 1:
    print(f'{u} {d}')
else:
    print(f'{u // gcd(u, d)} {d // gcd(u, d)}')
