import heapq

queue = []
n = int(input())
for i in range(n):
    heapq.heappush(queue, (int(input())))

res = 0
while len(queue) > 1:
    a = heapq.heappop(queue)
    b = heapq.heappop(queue)
    heapq.heappush(queue, a + b)
    res += (a + b)
print(res)
