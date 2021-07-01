answer = 0


def dfs(numbers, num, target, length):
    global answer
    if length == len(numbers):
        if num == target:
            answer += 1
            return
        else:
            return
    else:
        dfs(numbers, num + numbers[length], target, length + 1)
        dfs(numbers, num - numbers[length], target, length + 1)


def solution(numbers, target):
    global answer
    dfs(numbers, numbers[0], target, 1)
    dfs(numbers, -numbers[0], target, 1)
    return answer


print(solution([1, 1, 1, 1, 1], 3))
