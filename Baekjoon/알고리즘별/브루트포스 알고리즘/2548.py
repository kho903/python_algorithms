# 시간 초과 남
# n = int(input())
# lst = list(map(int, input().split()))
# lst.sort()
# lst_set = list(set(lst))
# lst_oper = []
# for s in lst_set:
#     lst_oper.append(sum([abs(a-s) for a in lst]))
# print(lst_set[lst_oper.index(min(lst_oper))])

# 중앙값을 이용하여 품
n = int(input())
lst = list(map(int, input().split()))
lst.sort()
if lst[n // 2 - 1] <= lst[n // 2]:
    print(lst[n // 2 - 1])
else:
    print(lst[n // 2])
