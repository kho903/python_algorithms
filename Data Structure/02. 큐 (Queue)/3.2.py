import queue

# 3.2 LifoQueue() 로 큐 만들기 (LILO(Last-In Last-out))

data_queue = queue.LifoQueue()
data_queue.put("a")
data_queue.put("b")
print(data_queue.qsize())   # 2
print(data_queue.get())     # b
