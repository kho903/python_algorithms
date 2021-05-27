def is_prime(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


n = int(input())
num_list = list(map(int, input().split()))
res = 0
for x in num_list:
    if is_prime(x):
        res += 1
print(res)
