def solution(arr):
    m = min(arr)
    answer = []
    for a in arr:
        if a != m:
            answer.append(a)
    if not answer:
        return [-1]
    return answer


print(solution([4, 3, 2, 1]))
print(solution([10]))
