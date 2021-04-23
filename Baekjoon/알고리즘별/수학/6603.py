from itertools import combinations
while True:
    n, *arr = map(int, input().split())
    if n == 0:
        break
    for a in list(combinations(arr, 6)):
        print(*a)
    print()
