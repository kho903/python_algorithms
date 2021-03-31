n = int(input())
count = 0
for i in range(n):
    number = list(map(int, input().split()))
    avg = sum(number[1:]) / number[0]
    for j in number[1:]:
        if j > avg:
            count += 1
    print("%.3f" % (count * 100 / number[0]), end="")
    print("%")
    count = 0
