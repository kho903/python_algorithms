def solution(s):
    answer = ''
    slist = s.split(' ')
    for a in slist:
        for i in range(len(a)):
            if i % 2== 0:
                answer += a[i].upper()
            else:
                answer += a[i].lower()
    return answer[:-1]


print(solution("try hello world"))