res = []
for i in range(1, 10001):
    res.append(i)

for i in range(1, 10001):
    if (i + i) in res:
        res.remove(i + i)
    if i >= 10:
        if i + int(i % 10) in res:
            res.remove(i + int(i % 10))
        if i >= 100:
            if i + int(i % 10) + int(i/10 % 10) in res:
                res.remove(i + int(i % 10) + int(i/10 % 10))
            if i >= 1000:
                if i + int(i % 10) + int(i/10 % 10) + int(i/100 % 10) in res:
                    res.remove(i + int(i % 10) + int(i/10 % 10) + int(i/100 % 10))

print(res)
