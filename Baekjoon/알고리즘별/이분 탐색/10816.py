from collections import Counter

n = int(input())
num = list(map(int, input().split()))
res = Counter(num)
m = int(input())
find = list(map(int, input().split()))
for i in range(m):
    print(res[find[i]], end=' ')
