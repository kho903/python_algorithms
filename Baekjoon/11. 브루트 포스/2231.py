n = int(input())
for i in range(n):
    ans = i
    sum_n = 0
    sum_n += i
    while int(i / 10) != 0 or i % 10 != 0:
        sum_n += i % 10
        i = int(i / 10)
    if sum_n == n:
        print(ans)
        break
else:
    print(0)
