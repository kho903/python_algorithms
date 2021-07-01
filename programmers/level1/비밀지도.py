def solution(n, arr1, arr2):
    answer = [""] * n
    for i in range(n):
        arr1[i] = bin(arr1[i])[2:]
        arr2[i] = bin(arr2[i])[2:]
        if len(arr1[i]) < n:
            while len(arr1[i]) < n:
                arr1[i] = "0" + arr1[i]
        if len(arr2[i]) < n:
            while len(arr2[i]) < n:
                arr2[i] = "0" + arr2[i]
        for j in range(n):
            if arr1[i][j] == "0" and arr2[i][j] == "0":
                answer[i] += " "
            else:
                answer[i] += "#"
    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
