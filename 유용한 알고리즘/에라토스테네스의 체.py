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


print(prime_list(2))
print(prime_list(3))
print(prime_list(10))
print(prime_list(20))

