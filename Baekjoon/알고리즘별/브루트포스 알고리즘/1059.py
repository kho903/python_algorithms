from itertools import combinations

L = int(input())
s = list(map(int, input().split()))
n = int(input())
s.sort()
if n in s:
    print(0)
else:
    a, b = 0, 0
    for i in range(L - 1):
        if s[i] < n < s[i + 1]:
            a, b = s[i] + 1, s[i + 1]

    all_c = len(list(combinations(range(a, b), 2)))
    left_c = len(list(combinations(range(a, n), 2)))
    right_c = len(list(combinations(range(n + 1, b), 2)))
    print(all_c - left_c - right_c)

