import sys

m = int(sys.stdin.readline())
s = set()
for _ in range(m):
    a = sys.stdin.readline().split()
    if len(a) == 1:
        if a[0] == "all":
            s = set([i for i in range(1, 21)])
        elif a[0] == "empty":
            s = set()
    else:
        e = int(a[1])
        if a[0] == "add":
            s.add(e)
        elif a[0] == "check":
            if e in s:
                print(1)
            else:
                print(0)
        elif a[0] == "remove":
            if e in s:
                s.remove(e)
        elif a[0] == "toggle":
            if e in s:
                s.remove(e)
            else:
                s.add(e)
