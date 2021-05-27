def check(arr, start_row, end_row, start_col, end_col):
    ans = 1
    n = len(arr)
    for i in range(start_row, end_row + 1):
        cnt = 1
        for j in range(1, n):
            if arr[i][j] == arr[i][j - 1]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt:
                ans = cnt
    for i in range(start_col, end_col + 1):
        cnt = 1
        for j in range(1, n):
            if arr[j][i] == arr[j - 1][i]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt:
                ans = cnt
    return ans


n = int(input())
arr = [list(input()) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(n):
        if j + 1 < n:
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
            temp = check(arr, i, i, j, j + 1)
            if ans < temp:
                ans = temp
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
        if i + 1 < n:
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
            temp = check(arr, i, i + 1, j, j)
            if ans < temp:
                ans = temp
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]

print(ans)
