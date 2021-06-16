from collections import deque

a, b = map(int, input().split())
q = deque()
q.append((a, 1))
res = -1
while q:
    tob, i = q.popleft()
    if tob == b:
        res = i
        break
    if tob * 2 <= b:
        q.append((tob * 2, i + 1))
    if int(str(tob) + '1') <= b:
        q.append((int(str(tob) + '1'), i + 1))
print(res)
