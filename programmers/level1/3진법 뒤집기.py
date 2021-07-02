def solution(n):
    str3 = ''
    while n > 0:
        str3 += str(n % 3)
        n //= 3
    int3 = int(str3)
    ans = 0
    a = 1
    while int3> 0:
        ans += int3 % 10 * a
        int3 //= 10
        a *= 3

    return ans


print(solution(45))
print(solution(125))
