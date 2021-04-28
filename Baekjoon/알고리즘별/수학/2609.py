N, M = map(int, input().split())
n, m = N, M
while n != 0:
    m %= n
    n, m = m, n
print(m)
print(N * M // m)
