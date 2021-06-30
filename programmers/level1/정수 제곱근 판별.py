def solution(n):
    a = [i for i in range(1, 10000001)]
    for i in a:
        if i * i == n:
            return (i + 1) ** 2
        elif i > n:
            return -1


print(solution(121))
print(solution(3))
