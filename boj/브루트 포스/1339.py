n = int(input())
word = [input() for _ in range(n)]
alpha_dict = {}
for w in word:
    r = len(w) - 1
    for alpha in w:
        if alpha not in alpha_dict:
            alpha_dict[alpha] = 10 ** r
        elif alpha in alpha_dict:
            alpha_dict[alpha] += 10 ** r

        r -= 1
value_list = sorted(alpha_dict.values(), reverse=True)
k = 9
ans = 0
for v in value_list:
    ans += k * v
    k -= 1
print(ans)
