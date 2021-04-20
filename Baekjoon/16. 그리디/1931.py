n = int(input())
t = []
for _ in range(n):
    t.append(list(map(int, input().split())))

t.sort(key=lambda x: (x[1], x[0]))
result = 1
e = t[0][1]
for i in range(1, n):
    if t[i][0] >= e:
        result += 1
        e = t[i][1]

print(result)
