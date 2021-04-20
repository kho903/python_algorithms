n = input()
count = 0
for i in range(1, len(n)):
    if n[i] != n[i - 1]:
        count += 1

if count % 2 == 0:
    print(count // 2)
else:
    print(count // 2 + 1)
