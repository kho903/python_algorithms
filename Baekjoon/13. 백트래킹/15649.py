from itertools import permutations

n, m = map(int, input().split())
n_list = [x for x in range(1, n + 1)]
p = list(permutations(n_list, m))
# print(p)
for i in range(len(p)):
    for j in range(len(p[i])):
        print(p[i][j], end=' ')
    print()