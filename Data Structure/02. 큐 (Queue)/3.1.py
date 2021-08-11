import queue

# 3.1 Queue() 로 큐 만들기 (가장 일반적인 큐, FIFO(First-In First-out))

data_queue = queue.Queue()
data_queue.put("a")
data_queue.put(1)
print(data_queue.qsize())   # 2
print(data_queue.get())     # a
print(data_queue.qsize())   # 1
