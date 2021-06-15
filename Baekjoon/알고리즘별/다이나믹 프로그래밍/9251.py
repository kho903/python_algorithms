a = input()
b = input()
len_a = len(a)
len_b = len(b)
d = [[0] * (len_b + 1) for _ in range(len_a + 1)]

for i in range(1, len_a + 1):
    for j in range(1, len_b + 1):
        if a[i - 1] == b[j - 1]:
            d[i][j] = d[i - 1][j - 1] + 1
        else:
            d[i][j] = max(d[i - 1][j], d[i][j - 1])

print(d[-1][-1])
