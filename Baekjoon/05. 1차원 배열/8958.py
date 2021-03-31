n = int(input())
for i in range(n):
    ox = list(input())
    sum_value = 0
    v = 1
    for j in ox:
        if j == 'O':
            sum_value += v
            v += 1
        else:
            v = 1
    print(sum_value)
