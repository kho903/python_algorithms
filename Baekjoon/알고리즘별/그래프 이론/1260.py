n, m, v = map(int, input().split())
g = []
for _ in range(n + 1):
    g.append([])
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

for gg in g:
    gg.sort()


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)
dfs(g, v, visited_dfs)
print()
bfs(g, v, visited_bfs)
