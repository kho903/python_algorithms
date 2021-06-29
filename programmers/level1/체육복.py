def solution(n, lost, reserve):
    reserve2 = [i for i in reserve if i not in lost]
    lost2 = [i for i in lost if i not in reserve]
    for i in reserve2:
        left = i - 1
        right = i + 1
        if left in lost2:
            lost2.remove(left)
        elif right in lost2:
            lost2.remove(right)
    return n - len(lost2)


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
