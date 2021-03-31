word = input()
res = []
for i in range(26):
    res.append(-1)

for i in range(len(word)):
    if res[ord(word[i]) - 97] == -1:
        res[ord(word[i]) - 97] = i

for i in res:
    print(i, end=" ")
