n = int(input())
a = 1
plus_value6 = 6
answer = 1
if n == 1:
    print(1)
else:
    while True:
        a += plus_value6
        answer += 1
        if a >= n:
            print(answer)
            break
        plus_value6 += 6
