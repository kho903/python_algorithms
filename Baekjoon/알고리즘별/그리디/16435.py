n, L = map(int, input().split())
h = list(map(int, input().split()))
h.sort()

for i in range(n):
    if L >= h[i]:
        L += 1

print(L)