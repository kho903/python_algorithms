n = int(input())
a = list(map(int, input().split()))
m = int(input())
input_list = list(map(int, input().split()))
a.sort()


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0


for i in range(m):
    print(binary_search(a, input_list[i], 0, len(a) - 1))
