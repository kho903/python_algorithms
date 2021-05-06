from collections import deque

n = int(input())

queue = deque([i for i in range(1, n + 1)])
i = 1
while len(queue) > 1:
    if i % 2 != 0:
        queue.popleft()
    else:
        queue.append(queue.popleft())
    i += 1
print(queue[0])
