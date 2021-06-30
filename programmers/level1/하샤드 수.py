def solution(x):
    s = sum(list(map(int, str(x))))
    if x % s == 0:
        return True
    else:
        return False


print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))