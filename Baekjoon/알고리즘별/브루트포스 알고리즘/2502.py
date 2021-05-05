d, k = map(int, input().split())
a = 1
b = 1
first_a = 1
first_b = 1
to_d = 2
i = 1
while True:
    res = (a + b)
    a = b
    b = res
    to_d += 1
    if res > k:
        first_a += 1
        first_b += 1
        a = first_a
        b = first_b
        to_d = 2
        i = 1
    if to_d == d:
        if res == k:
            print(first_a, first_b + i - 1, sep='\n')
            break
        else:
            a = first_a
            b = first_b + i
            to_d = 2
            i += 1
