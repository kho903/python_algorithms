t = int(input())
a, b, c = 300, 60, 10
abc = [a, b, c]
res = []
for i in range(3):
    res.append(t // abc[i])
    t %= abc[i]
if t == 0:
    print(res[0], res[1], res[2])
else:
    print(-1)
