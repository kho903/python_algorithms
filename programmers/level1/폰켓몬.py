def solution(nums):
    answer = 0
    set_len = len(set(nums))
    if set_len > len(nums) // 2:
        return len(nums) // 2
    else:
        return set_len


print(solution([3, 1, 2, 3]))
print(solution([3, 3, 3, 2, 2, 4]))
print(solution([3, 3, 3, 2, 2, 2]))
