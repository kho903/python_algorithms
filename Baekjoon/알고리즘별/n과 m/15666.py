from itertools import combinations_with_replacement

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
res = list(combinations_with_replacement(a, m))
res = sorted(list(set(res)))

for i in res:
    print(*i)
