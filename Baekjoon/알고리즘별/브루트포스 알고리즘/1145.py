num_list = list(map(int, input().split()))
min_v = min(num_list)

while True:
    count = 0
    for i in range(5):
        if min_v % num_list[i] == 0:
            count += 1
    if count >= 3:
        print(min_v)
        break
    min_v += 1
