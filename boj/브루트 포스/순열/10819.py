def next_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i - 1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a) - 1
    while a[j] <= a[i - 1]:
        j -= 1
    a[i - 1], a[j] = a[j], a[i - 1]
    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True


def calc(a):
    res = 0
    for i in range(1, len(a)):
        res += abs(a[i] - a[i - 1])
    return res


n = int(input())
a = list(map(int, input().split()))
a.sort()
res = 0
while True:
    res = max(res, calc(a))
    if not next_permutation(a):
        break

print(res)
