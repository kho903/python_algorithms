def gcd(a, b):
    if b > a:
        a, b = b, a
    while b != 0:
        a %= b
        a, b = b, a
    return a


n, s = map(int, input().split())
a = list(map(int, input().split()))

new_a = [abs(x - s) for x in a]
prev = new_a[0]
g = new_a[0]
for i in range(1, len(new_a)):
    g = gcd(prev, new_a[i])
    prev = g

print(g)
