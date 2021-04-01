n = int(input())
num_list = list(map(int, input().split()))
count = 0
for num in num_list:
    if num == 2:
        count += 1
    elif num > 2:
        for i in range(2, num):
            if num % i == 0:
                break
            if i == num - 1:
                count += 1
print(count)
