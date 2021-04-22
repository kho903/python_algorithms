while True:
    arr = list(map(int, input().split()))
    if arr == [-1]:
        break
    arr.pop()
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] * 2 == arr[j] or arr[i] / 2 == arr[j]:
                count += 1
    print(count)