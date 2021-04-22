m = []
for _ in range(10):
    m.append(int(input()))

s = 0
for i in range(10):
    s += m[i]
    if s >= 100:
        if s - 100 > 100 - (s - m[i]):
            s -= m[i]
            break

print(s)
