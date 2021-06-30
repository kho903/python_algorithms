def prime_list(n):
    # 에라토스테네스의 체 초기화 : n개의 요소에 True 설정 (소수로 간주)
    a = [True] * (n + 1)

    # n의 최대 약수가 sqrt(n) 이하이므로 ui = sqrt(n)까지 검사
    m = int((n + 1) ** 0.5)
    for i in range(2, m + 1):
        if a[i]:
            for j in range(i + i, n + 1, i):
                a[j] = False
    return len([i for i in range(2, n + 1) if a[i] == True])


print(prime_list(10))
print(prime_list(5))