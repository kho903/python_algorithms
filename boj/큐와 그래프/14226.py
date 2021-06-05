from collections import deque

s = int(input())
dist = [[-1] * (s + 1) for i in range(s + 1)]
q = deque()
q.append((1, 0))
dist[1][0] = 0
while q:
    e, c = q.popleft()
    if dist[e][e] == -1:
        dist[e][e] = dist[e][c] + 1
        q.append((e, e))
    if e + c <= s and dist[e + c][c] == -1:
        dist[e + c][c] = dist[e][c] + 1
        q.append((e + c, c))
    if e - 1 >= 0 and dist[e - 1][c] == -1:
        dist[e - 1][c] = dist[e][c] + 1
        q.append((e - 1, c))
ans = -1
for i in range(s + 1):
    if dist[s][i] != -1:
        if ans == -1 or ans > dist[s][i]:
            ans = dist[s][i]
print(ans)
