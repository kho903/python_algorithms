def solution(x, n):
    answer = []
    s = x
    for i in range(1, n + 1):
        answer.append(s * i)
    return answer


print(solution(2, 5))
print(solution(4, 3))
print(solution(-4, 2))
