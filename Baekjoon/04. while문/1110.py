start = temp = int(input())
i = 0

while True:
    a = temp // 10
    b = temp % 10
    i += 1
    temp = b * 10 + (a + b) % 10
    if temp == start:
        break

print(i)