def fact(n):
    if n == 1 or n == 0:
        return 1
    return n * fact(n - 1)


n = int(input())

fact_n = fact(n)
count = 0
while True:
    if fact_n % 10 != 0:
        break
    fact_n //= 10
    count += 1
print(count)
