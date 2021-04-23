from itertools import permutations

n = int(input())
all_num = list(map(int, input().split()))
a_per = list(permutations(all_num))

r = 0
for element in a_per:
    s = 0
    list_el = list(element)
    for i in range(1, n):
        s += abs(list_el[i] - list_el[i - 1])
    r = max(s, r)
print(r)
