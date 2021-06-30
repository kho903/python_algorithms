def solution(s, n):
    answer = ''
    low = 'abcdefghijklmnopqrstuvwxyz'
    up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for a in s:
        if a.islower():
            if low.index(a) + n > 25:
                answer += low[low.index(a) + n - 26]
            else:
                answer += low[low.index(a) + n]
        elif a.isupper():
            if up.index(a) + n > 25:
                answer += up[up.index(a) + n - 26]
            else:
                answer += up[up.index(a) + n]
        else:
            answer += " "
    return answer


print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))
