n = list(input())
n.sort(reverse=True)
s = 0
for i in n:
    s += int(i)
if n[-1] != '0' or s % 3 != 0:
    print(-1)
else:
    print("".join(n))
