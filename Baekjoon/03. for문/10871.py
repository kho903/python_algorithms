num, m = map(int, input().split())
num_list = list(map(int, input().split()))
for i in range(num):
    if num_list[i] < m:
        print(num_list[i], end=" ")
