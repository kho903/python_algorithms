# 리스트 변수로 스택을 다루는 pop, push 기능 구현해보기
# (pop, push 함수 사용하지 않고 직접 구현해 보기)
stack_list = list()


def push(data):
    stack_list.append(data)


def pop():
    data = stack_list[-1]
    del stack_list[-1]
    return data


for i in range(10):
    push(i)
print(stack_list)
print(pop())
print(stack_list)
