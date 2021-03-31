remainder_list = []
for i in range(10):
    remainder_list.append(int(input()) % 42)

remainder_list = set(remainder_list)
print(len(remainder_list))