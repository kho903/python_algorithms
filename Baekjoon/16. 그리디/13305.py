n = int(input())
km = list(map(int, input().split()))
price = list(map(int, input().split()))
p = [price[0]]
res = km[0] * price[0]
m = p[0]
for i in range(1, n - 1):
    p.append(price[i])
    if price[i] < m:
        res += km[i] * price[i]
        m = price[i]
    else:
        res += km[i] * m
print(res)
