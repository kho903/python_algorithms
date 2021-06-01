n = int(input())
t = [0] * (n + 1)
p = [0] * (n + 1)
for i in range(1, n + 1):
    t[i], p[i] = map(int, input().split())
res = 0


def calc(day, s):
    global res
    if day == n + 1:
        res = max(res, s)
        return
    if day > n + 1:
        return
    calc(day + 1, s)
    calc(day + t[day], s + p[day])


calc(1, 0)
print(res)
