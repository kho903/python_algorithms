t = int(input())


def prime_list(n):
    # 에라토스테네스의 체 초기화 : n개의 요소에 True 설정 (소수로 간주)
    a = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 ui = sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if a[i]:
            for j in range(i + i, n, i):
                a[j] = False
    return [i for i in range(2, n) if a[i] == True]


def print_all_sum(prime, p):
    for a in prime:
        for b in prime:
            for c in prime:
                if a + b + c == p:
                    print(a, b, c)
                    return
    print(0)


for _ in range(t):
    k = int(input())
    k_prime = prime_list(k)
    print_all_sum(k_prime, k)
