from collections import Counter

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a_sum = []
b_sum = []
for i in range(n):
    s = 0
    for j in range(i, n):
        s += a[j]
        a_sum.append(s)

for i in range(m):
    s = 0
    for j in range(i, m):
        s += b[j]
        b_sum.append(s)

a_sum.sort()
b_sum.sort()
c = Counter(b_sum)
ans = 0
for e in a_sum:
    ans += c[t - e]
print(ans)
