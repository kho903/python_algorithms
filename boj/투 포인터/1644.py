def is_prime_array(n):
    a = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if a[i]:
            for j in range(i + i, n, i):
                a[j] = False
    return [i for i in range(2, n) if a[i] == True]


n = int(input())
a = is_prime_array(n + 1)

left = right = 0
sum_res = 0 if len(a) == 0 else a[0]
ans = 0
while left <= right < len(a):
    if sum_res < n:
        right += 1
        if right < len(a):
            sum_res += a[right]
    elif sum_res == n:
        ans += 1
        right += 1
        if right < len(a):
            sum_res += a[right]
    elif sum_res > n:
        sum_res -= a[left]
        left += 1
        if right < left < len(a):
            right = left
            sum_res = a[left]

print(ans)
