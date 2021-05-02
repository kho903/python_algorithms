import sys

n = int(sys.stdin.readline())
stack = []


def push(x):
    stack.append(x)


def top():
    return stack[-1] if stack else -1


def pop():
    return stack.pop(-1) if stack else -1


def empty():
    return 0 if stack else 1


def size():
    return len(stack)


for _ in range(n):
    input_value = sys.stdin.readline().split()
    order = input_value[0]
    if order == "push":
        push(input_value[1])
    elif order == "top":
        print(top())
    elif order == "size":
        print(size())
    elif order == "empty":
        print(empty())
    elif order == "pop":
        print(pop())
