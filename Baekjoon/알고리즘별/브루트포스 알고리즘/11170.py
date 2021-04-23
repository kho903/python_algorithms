t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    count = 0
    for e in range(n, m + 1):
        a = list(str(e))
        for i in range(len(a)):
            if a[i] == '0':
                count += 1
    print(count)
