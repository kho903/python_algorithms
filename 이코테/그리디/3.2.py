# n이 1이 될때까지 
# n 에서 1빼기
# n을 k로 나눈다. (n이 k로 나누어 떨어질 때만)

# # 내가 짠 코드
# n, k = map(int, input().split())
# count = 0
#
# while n != 1:
#     if n % k == 0:
#         n //= k
#     else:
#         n -= 1
#     count += 1
#
# print(count)

# 강의 코드 -- 시간복잡도가 log로 나타나서 훨씬 효율적
n, k = map(int, input().split())
result = 0

while True:
    # n이 k로 나누어 떨어지는 수가 될때까지 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # n이 k보다 작을때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # k로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)
