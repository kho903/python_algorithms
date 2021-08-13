def sum_all(n):
    # 시간 복잡도 구하기
    # 입력 n에 따라 덧셈을 n번 해야함 (반복문)
    # 시간 복잡도 : n, 빅오 표기법으로는 O(n)
    total = 0
    for num in range(1, n + 1):
        total += num
    return total


def sum_all2(n):
    # 시간 복잡도 구하기
    # 입력 n이 어떻든 간에, 곱셈 / 덧셈 / 나눗셈 하면 됨(반복문이 없음)
    # 시간 복잡도 : 1, O(1)
    return int(n * (n + 1) / 2)


print(sum_all(100))
print(sum_all2(100))

# O(n) vs O(1)
# 이와 같이 동일한 문제를 푸는 알고리즘은 다양할 수 있음
# 어느 알고리즘이 보다 좋은지를 객관적으로 비교하기 위해
# 빅 오 표기법 등의 시간복잡도 계산법을 사용함
