n = int(input())
for _ in range(n):
    stack = []
    sentense = input()
    res = ''
    for s in sentense:
        if s == ' ':
            while stack:
                res += stack.pop()
            res += ' '
        else:
            stack.append(s)
    while stack:
        res += stack.pop()
    print(res)
