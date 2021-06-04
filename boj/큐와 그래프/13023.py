import sys

n, m = map(int, input().split())
edges = []  # 간선 리스트
a = [[False] * n for _ in range(n)]  # 인접 행렬
g = [[] for _ in range(n)]  # 인접 리스트
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))
    edges.append((v, u))  # 양방향
    a[u][v] = a[v][u] = True  # 인접행렬 양 방향 True
    g[u].append(v)
    g[v].append(u)
m *= 2  # 양방향이므로 간선 개수 * 2
for i in range(m):
    for j in range(m):
        A, B = edges[i]  # A -> B
        C, D = edges[j]  # C -> D
        if A == B or A == C or A == D or B == C or B == D or C == D:
            continue
        if not a[B][C]:  # B -> C 확인 위해 인접 행렬 이용
            continue
        for E in g[D]:  # D -> E 확인 위해 인접 리스트
            if A == E or B == E or C == E or D == E:
                continue
            print(1)
            sys.exit()
print(0)
