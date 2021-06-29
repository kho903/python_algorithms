def solution(left, right):
    answer = 0
    square = []
    for i in range(32):
        square.append(i ** 2)
    for i in range(left, right + 1):
        if i in square:
            answer -= i
        else:
            answer += i
    return answer


print(solution(13, 17))
print(solution(24, 27))
