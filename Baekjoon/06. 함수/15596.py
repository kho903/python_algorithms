def solve(a: list):
    ans = 0
    for i in a:
        ans += i
    return ans


q = [1, 2, 3, 4]
w = [2, 3, 4]
print(solve(q))
print(solve(w))
