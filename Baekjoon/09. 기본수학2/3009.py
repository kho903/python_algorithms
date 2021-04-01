x = []
y = []
for _ in range(3):
    x1, y1 = map(int, input().split())
    x.append(x1)
    y.append(y1)
x_a = 0
y_a = 0

for i in range(3):
    if x.count(x[i]) == 1:
        x_a = x[i]
    if y.count(y[i]) == 1:
        y_a = y[i]

print(x_a, y_a)
