def solution(d, budget):
    d.sort()
    res = 0
    for a in d:
        if budget >= a:
            res += 1
            budget -= a
    return res


solution([1,3,2,5,4],9)
solution([2,2,3,3], 10)
