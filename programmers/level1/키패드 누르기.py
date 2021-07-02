def solution(numbers, hand):
    answer = ''
    t_l = 10
    t_r = 12
    if hand == 'right':
        h = 'R'
    else:
        h = 'L'
    for n in numbers:
        if n == 0:
            n = 11
        if n in [1, 4, 7]:
            answer += 'L'
            t_l = n
        elif n in [3, 6, 9]:
            answer += 'R'
            t_r = n
        elif n in [2, 5, 8, 11]:
            l = abs(n - t_l)
            r = abs(n - t_r)
            if sum(divmod(l, 3)) > sum(divmod(r, 3)):
                answer += 'R'
                t_r = n
            elif sum(divmod(r, 3)) > sum(divmod(l, 3)):
                answer += 'L'
                t_l = n
            else:
                answer += h
                if h == 'R':
                    t_r = n
                else:
                    t_l = n
            # if t_l in [n - 3, n - 1, n + 3] and t_r in [n - 3, n + 1, n + 3]:
            #     answer += h
            #     if h == 'R':
            #         t_r = n
            #     else:
            #         t_l = n
            # elif t_l in [n - 3, n - 1, n + 3]:
            #     answer += 'L'
            #     t_l = n
            # elif t_r in [n - 3, n + 1, n + 3]:
            #     answer += 'R'
            #     t_r = n
            # elif t_l in [n - 4, n + 2] and t_r in [n - 2, n + 4]:
            #     answer += h
            #     if h == 'R':
            #         t_r = n
            #     else:
            #         t_l = n
            # elif t_l in [n - 4, n + 2]:
            #     answer += 'L'
            #     t_l = n
            # elif t_r in [n - 2, n + 4]:
            #     answer += 'R'
            #     t_r = n
            # elif t_l in [n - 6, n + 6] and t_r in [n - 6, n + 6]:
            #     answer += h
            #     if h == 'R':
            #         t_r = n
            #     else:
            #         t_l = n
            # elif t_l in [n - 6, n + 6]:
            #     answer += 'L'
            #     t_l = n
            # elif t_r in [n - 6, n + 6]:
            #     answer += 'R'
            #     t_r = n
            # elif t_l in [n - 7, n + 7] and t_r in [n - 5, n + 5]:
            #     answer += h
            #     if h == 'R':
            #         t_r = n
            #     else:
            #         t_l = n
            # elif t_l in [n - 7, n + 7]:
            #     answer += 'L'
            #     t_l = n
            # elif t_r in [n - 5, n + 5]:
            #     answer += 'R'
            #     t_r = n
            # elif t_l in [n - 9, n + 9] and t_r in [n - 9, n + 9]:
            #     answer += h
            #     if h == 'R':
            #         t_r = n
            #     else:
            #         t_l = n
            # elif t_l in [n - 9, n + 9]:
            #     answer += 'L'
            #     t_l = n
            # elif t_r in [n - 9, n + 9]:
            #     answer += 'R'
            #     t_r = n
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))
