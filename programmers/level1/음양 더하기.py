def solution(absolutes, signs):
    n = len(absolutes)
    answer = 0
    for i in range(n):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer


print(solution([4,7,12], [True,False, True]))
print(solution([1,2,3], [False,False, True]))