def solve(a, index, cur, plus, minus, multi, div):
    if index == len(a):
        return (cur, cur)
    res = []
    if plus:
        res.append(solve(a, index + 1, cur + a[index], plus - 1, minus, multi, div))
    if minus:
        res.append(solve(a, index + 1, cur - a[index], plus, minus - 1, multi, div))
    if multi:
        res.append(solve(a, index + 1, cur * a[index], plus, minus, multi - 1, div))
    if div:
        if cur >= 0:
            res.append(solve(a, index + 1, cur // a[index], plus, minus, multi, div - 1))
        else:
            res.append(solve(a, index + 1, -(-cur // a[index]), plus, minus, multi, div - 1))
    ans = (
        max([t[0] for t in res]),
        min([t[1] for t in res])
    )
    return ans


n = int(input())
a = list(map(int, input().split()))
plus, minus, multi, div = map(int, input().split())
ans = solve(a, 1, a[0], plus, minus, multi, div)
print(ans[0])
print(ans[1])
