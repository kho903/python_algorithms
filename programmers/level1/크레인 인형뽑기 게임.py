def solution(board, moves):
    answer = 0
    a = []
    s = 0
    while s < len(moves):
        for i in range(len(board)):
            if board[i][moves[s] - 1] != 0:
                a.append(board[i][moves[s] - 1])
                board[i][moves[s] - 1] = 0
                break
        s += 1
    while True:
        d = False
        for i in range(1, len(a)):
            if a[i] == a[i - 1]:
                a = a[:i-1] + a[i + 1:]
                answer += 2
                d = True
                break
        if not d:
            break
    return answer


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
               [1, 5, 3, 5, 1, 2, 1, 4]))
