def solution(brown, yellow):
    sum_v = brown + yellow
    for i in range(1, sum_v // 2):
        if sum_v % i == 0:
            w = i
            h = sum_v // i
            if (w - 2) * (h - 2) == yellow:
                return [h, w]


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
print(solution(18, 6))
