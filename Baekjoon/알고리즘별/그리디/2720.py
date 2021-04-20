n = int(input())
# a = [0.25, 0.1, 0.05, 0.01]
a = [25, 10, 5, 1]
for _ in range(n):
    p = int(input())
    for i in a:
        print(p // i, end=' ')
        p %= i
    print()
