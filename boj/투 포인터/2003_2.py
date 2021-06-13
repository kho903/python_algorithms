n, m = map(int, input().split())
a = list(map(int, input().split()))
left = right = 0
sum_res = a[0]
ans = 0
while left <= right < n:
    if sum_res < m:
        right += 1
        if right < n:
            sum_res += a[right]
    elif sum_res == m:
        ans += 1
        right += 1
        if right < n:
            sum_res += a[right]
    elif sum_res > m:
        sum_res -= a[left]
        left += 1
        if right < left < n:
            right = left
            sum_res = a[left]
print(ans)
