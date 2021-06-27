def solution(n):
    if n <= 3:
        return "124"[n - 1]
    else:
        n, m = divmod(n - 1, 3)
        return solution(n) + "124"[m]


print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
