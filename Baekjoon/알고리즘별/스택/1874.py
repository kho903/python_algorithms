n = int(input())
stack = []
count = 1
to_print = []
flag = True
for _ in range(n):
    num = int(input())
    while count <= num:
        stack.append(count)
        to_print.append('+')
        count += 1
    if stack[-1] == num:
        to_print.append('-')
        stack.pop()
    else:
        flag = False
if not flag:
    print("NO")
else:
    for e in to_print:
        print(e)
