a, b = input().split()
len_b_a = len(b) - len(a)
min_count = 50
for i in range(len_b_a + 1):
    count = 0
    for j in range(len(a)):
        if a[j] != b[i + j]:
            count += 1
    min_count = min(count, min_count)

print(min_count)
