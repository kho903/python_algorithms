a, b = map(int, input().split())


def dfs(lower, upper, depth, num):
    ans = 0
    if num > upper:
        return 0
    if depth >= 10:
        return 0
    if lower <= num <= upper:
        ans += 1
    ans += dfs(lower, upper, depth + 1, num * 10 + 4)
    ans += dfs(lower, upper, depth + 1, num * 10 + 7)
    return ans


res = dfs(a, b, 0, 0)
print(res)
