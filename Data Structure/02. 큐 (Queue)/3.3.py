import queue

# 3.3 PriorityQueue() 로 큐 만들기

data_queue = queue.PriorityQueue()
# (우선순위, 데이터)
data_queue.put((10, "Korea"))
data_queue.put((5, 1))
data_queue.put((15, "China"))
print(data_queue.qsize())
print(data_queue.get())
print(data_queue.get())
print(data_queue.get())
