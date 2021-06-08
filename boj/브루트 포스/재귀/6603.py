def solve(a, index, lotto):
    if len(lotto) == 6:
        print(' '.join(map(str, lotto)))
    if index == len(a):
        return
    solve(a, index + 1, lotto + [a[index]])
    solve(a, index + 1, lotto)


while True:
    n, *a = list(map(int, input().split()))
    if n == 0:
        break
    solve(a, 0, [])
    print()
