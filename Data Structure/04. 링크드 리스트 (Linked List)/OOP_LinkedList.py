# 파이썬 객체지향 프로그래밍으로 링크드 리스트 구현하기
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == "":
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self, data):
        if self.head == "":
            print("해당 값을 가진 노드가 없습니다.")
            return
        # 1. head 삭제
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next


# linkedList1 = NodeMgmt(0)
# # linkedList1.desc()
#
# for data in range(1, 10):
#     linkedList1.add(data)
#
# linkedList1.desc()

linkedlist1 = NodeMgmt(0)
linkedlist1.desc()

# head가 살아있음을 확인
print(linkedlist1.head)

# head를 지운다.
linkedlist1.delete(0)
print(linkedlist1.head)  # None : 삭제 완료

# 다시 하나의 노드를 만들어 본다.
linkedlist1 = NodeMgmt(0)
for data in range(1, 10):
    linkedlist1.add(data)
linkedlist1.desc()  # 0~9
linkedlist1.delete(4)  # 4 삭제
linkedlist1.desc()  # 0 1 2 3 5 6 7 8 9
