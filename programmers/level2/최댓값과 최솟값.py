def solution(s):
    answer = ''
    a = s.split(' ')
    for i in range(len(a)):
        a[i] = int(a[i])
    answer += str(min(a)) + ' '
    answer += str(max(a))
    return answer

print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))