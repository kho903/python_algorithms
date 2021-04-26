import math

s = input()
t = input()

res = False

if len(s) == len(t):
    if s == t:
        res = True
else:
    to_s = len(t) // math.gcd(len(s), len(t))
    to_t = len(s) // math.gcd(len(s), len(t))
    s *= to_s
    t *= to_t
    if s == t:
        res = True

print(int(res))
