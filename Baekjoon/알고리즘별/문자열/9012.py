n = int(input())

for _ in range(n):
    p = list(input())
    sum = 0
    for a in p:
        if sum == 0 and a == ')':
            sum = -1
            break
        elif a == '(':
            sum += 1
        elif a == ')':
            sum -= 1
    if sum == 0:
        print("YES")
    else:
        print("NO")
