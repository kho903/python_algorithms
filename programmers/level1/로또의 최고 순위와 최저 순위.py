def solution(lottos, win_nums):
    answer = [6, 6, 5, 4, 3, 2, 1]
    zero = 0
    count = 0
    for num in lottos:
        if num == 0:
            zero += 1
        elif num in win_nums:
            count += 1
    return [answer[count + zero], answer[count]]


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))
