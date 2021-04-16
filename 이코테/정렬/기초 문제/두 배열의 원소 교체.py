# 내가 푼 방법
"""
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()

a_i = 0
b_i = len(b) - 1
for _ in range(k):
    if a[a_i] >= b[b_i]:
        break
    a[a_i], b[b_i] = b[b_i], a[a_i]
    a_i += 1
    b_i -= 1

print(sum(a))
"""

# 강의
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()  # a는 오름차순
b.sort(reverse=True)  # b는 내림차순

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k):
    # A의 원소가 B의 원소보다 작은 겨웅
    if a[i] < b[i]:
        # 두원소를 교체
        a[i], b[i] = b[i], a[i]
    else:  # A의 원소가 B의 원소볻가 크거나 같을 때, 반복문을 탈출
        break

print(sum(a))
