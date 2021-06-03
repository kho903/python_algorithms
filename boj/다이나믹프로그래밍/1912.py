n = int(input())
a = list(map(int, input().split()))
dp = [0] * n
dp[0] = a[0]
for i in range(n):
    if a[i] + dp[i - 1] > a[i]:
        dp[i] = a[i] + dp[i - 1]
    else:
        dp[i] = a[i]
print(max(dp))
