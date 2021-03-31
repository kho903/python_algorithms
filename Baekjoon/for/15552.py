import sys

a = int(sys.stdin.readline())
res = []

for i in range(a):
    first, second = sys.stdin.readline().rstrip().split()
    res.append(int(first) + int(second))

for i in range(a):
    print(res[i])
