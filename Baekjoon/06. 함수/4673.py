num = list(range(1, 10001))

i = 1
while i < 10001:
    result = i
    for a in str(i):
        result += int(a)
    if result in num:
        num.remove(result)
    i += 1

for i in num:
    print(i)
