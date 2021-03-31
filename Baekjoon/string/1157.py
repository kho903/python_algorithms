import collections

word = input().upper()
a = collections.Counter(word)
max_v = max(list(a.values()))
res = []
for i in list(a.keys()):
    if a[i] == max_v:
        res.append(i)

if len(res) > 1:
    print('?')
else:
    print(max(word, key=a.get))
