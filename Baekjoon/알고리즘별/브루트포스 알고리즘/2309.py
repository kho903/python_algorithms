n = []
for _ in range(9):
    n.append(int(input()))

s = sum(n)
a = 0
b = 0
n.sort()

for i in range(9):
    for j in range(i + 1, 9):
        if s - n[i] - n[j] == 100:
            a, b = i, j
            break
for i in range(9):
    if i != a and i != b:
        print(n[i])


