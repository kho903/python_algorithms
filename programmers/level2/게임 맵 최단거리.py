from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solution(maps):
    answer = 0
    h = len(maps)
    w = len(maps[0])
    d = [[-1] * w for _ in range(h)]
    q = deque()
    q.append([0, 0])
    d[0][0] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if maps[nx][ny] == 1:
                    if d[nx][ny] == -1:
                        d[nx][ny] = d[x][y] + 1
                        q.append([nx, ny])
    answer = d[-1][-1]

    return answer


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))
