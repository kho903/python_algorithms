def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def solution(arr):
    answer = 1
    for i in range(len(arr)):
        answer *= arr[i] // gcd(arr[i], answer)
    return answer


print(solution([2, 6, 8, 14]))
print(solution([1, 2, 3]))
