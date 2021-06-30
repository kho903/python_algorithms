def gcd(n, m):
    while m:
        n, m = m, n % m
    return n


def solution(n, m):
    return [gcd(n, m), n * m // gcd(n, m)]


print(solution(3, 12))
print(solution(2, 5))
