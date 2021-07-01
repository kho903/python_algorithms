# 통과 - 효율성 별로
def solution(N, stages):
    answer = []
    rate = []
    for i in range(1, N + 1):
        p = 0
        t = 0
        for j in range(len(stages)):
            if stages[j] > i:
                p += 1
            elif stages[j] == i:
                p += 1
                t += 1
        if p == 0:
            rate.append(0)
        else:
            rate.append(t / p)
    for _ in range(N):
        max_i = rate.index(max(rate))
        answer.append(max_i + 1)
        rate[max_i] = -1

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
