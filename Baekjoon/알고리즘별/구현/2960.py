n, k = map(int, input().split())


def solve(n, k):
    ans = []
    for i in range(2, n + 1):
        for j in range(i, n + 1, i):
            if j not in ans:
                ans.append(j)
    return ans[k - 1]


print(solve(n, k))
