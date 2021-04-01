n = int(input())
if n > 1:
    a = 1
    while True:
        a += 1
        if n % a == 0:
            print(a)
            n = int(n / a)
            a -= 1
        if n == 1:
            break
