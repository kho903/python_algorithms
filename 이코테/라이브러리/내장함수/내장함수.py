# sum()
res = sum([1, 2, 3, 4, 5])
print(res)

# min(), max()
min_res = min(7, 3, 5, 2)
max_res = max(7, 3, 5, 2)
print(min_res, max_res)

# eval()
res = eval("(3+5)*7")
print(res)

# sorted()
res = sorted([9, 1, 8, 5, 4])
reverse_res = sorted([9, 1, 8, 5, 4], reverse=True)
print(res)
print(reverse_res)

# sorted() with key
arr = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]
res = sorted(arr, key=lambda x: x[1], reverse=True)
print(res)
