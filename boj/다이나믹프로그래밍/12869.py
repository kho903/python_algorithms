n = int(input())
scv = list(map(int, input().split()))
while len(scv) < 3:
    scv += [0]
d = [[[-1] * 61 for j in range(61)] for i in range(61)]


def solve(i, j, k):
    if i < 0:
        return solve(0, j, k)
    if j < 0:
        return solve(i, 0, k)
    if k < 0:
        return solve(i, j, 0)
    if i == 0 and j == 0 and k == 0:
        return 0

    ans = d[i][j][k]
    if ans != -1:
        return ans
    ans = 60
    if ans > solve(i - 1, j - 3, k - 9):
        ans = solve(i - 1, j - 3, k - 9)
    if ans > solve(i - 1, j - 9, k - 3):
        ans = solve(i - 1, j - 9, k - 3)
    if ans > solve(i - 3, j - 1, k - 9):
        ans = solve(i - 3, j - 1, k - 9)
    if ans > solve(i - 3, j - 9, k - 1):
        ans = solve(i - 3, j - 9, k - 1)
    if ans > solve(i - 9, j - 1, k - 3):
        ans = solve(i - 9, j - 1, k - 3)
    if ans > solve(i - 9, j - 3, k - 1):
        ans = solve(i - 9, j - 3, k - 1)
    ans += 1
    d[i][j][k] = ans
    return d[i][j][k]


print(solve(scv[0], scv[1], scv[2]))
