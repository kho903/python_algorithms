n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
s = 0
for i in range(len(a)):
    s += a[i]
    for j in range(i + 1, len(a)):
        s += a[j]

print(s)
