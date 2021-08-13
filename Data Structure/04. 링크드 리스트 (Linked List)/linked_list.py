# Node 구현
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# Node와 Node 연결하기 (포인터 활용)
node1 = Node(1)
node2 = Node(2)
node1.next = node2
head = node1


# 링크드 리스트로 데이터 추가하기
def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)


for i in range(3, 10):
    add(i)

# 링크드 리스트 데이터 출력하기 (검색하기)
node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)

# 링크드 리스트의 복잡한 기능1 (링크드 리스트 데이터 사이에 데이터를 추가)
node3 = Node(1.5)
node = head
search = True
while search:
    if node.data == 1:
        search = False
    else:
        node = node.next
node_next = node.next
node.next = node3
node3.next = node_next

print("=====================")
while node.next:
    print(node.data)
    node = node.next
print(node.data)

