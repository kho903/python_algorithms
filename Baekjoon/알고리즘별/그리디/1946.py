import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    rank = []
    for _ in range(n):
        a, b = map(int, input().split())
        rank.append((a, b))
    rank.sort()
    count = 1
    max_r = rank[0][1]
    for i in range(1, len(rank)):
        if rank[i][1] < max_r:
            count += 1
            max_r = rank[i][1]
    print(count)
