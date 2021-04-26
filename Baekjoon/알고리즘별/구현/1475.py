n = list(map(int, input()))
num_l = [0] * 9
for num in n:
    if num == 9:
        num_l[6] += 1
    else:
        num_l[num] += 1
if num_l[6] % 2 == 0:
    num_l[6] = num_l[6] // 2
else:
    num_l[6] = num_l[6] // 2 + 1

print(max(num_l))
