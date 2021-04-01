a = int(input())
b = int(input())
sosu_list = []
for i in range(a, b+1):
    if i == 2:
        sosu_list.append(i)
    elif i > 2:
        for j in range(2, i):
            if i % j == 0:
                break
            if j == i - 1:
                sosu_list.append(i)

if not sosu_list:
    print(-1)
else:
    print(sum(sosu_list))
    print(min(sosu_list))