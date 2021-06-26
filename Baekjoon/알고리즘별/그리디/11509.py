n = int(input())
h = list(map(int, input().split()))
d = [0] * (n + 1)
ans = 0
for i in range(n):
    if d[h[i]] == 0:
        ans += 1
        d[h[i] - 1] += 1
    else:
        d[h[i]] -= 1
        d[h[i] - 1] += 1

print(ans)
