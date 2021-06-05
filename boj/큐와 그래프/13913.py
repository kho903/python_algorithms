from collections import deque
import sys

MAX = 200000
sys.setrecursionlimit(MAX)
n, k = map(int, input().split())
q = deque()
check = [False] * (MAX + 1)
dist = [-1] * (MAX + 1)
path = [-1] * MAX
check[n] = True
dist[n] = 0
q.append(n)
while q:
    curr = q.popleft()
    for nxt in [curr - 1, curr + 1, 2 * curr]:
        if 0 <= nxt < MAX and check[nxt] == False:
            check[nxt] = True
            dist[nxt] = dist[curr] + 1
            path[nxt] = curr
            q.append(nxt)
    if check[k]:
        break
print(dist[k])


def print_path(n, k):
    if n != k:
        print_path(n, path[k])
    print(k, end=' ')


print_path(n, k)
