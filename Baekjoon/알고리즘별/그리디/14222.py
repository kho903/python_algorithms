n, k = map(int, input().split())
input_list = list(map(int, input().split()))
input_list.sort()
to_l = list(range(1, n + 1))

for num in input_list:
    if num in to_l:
        to_l.remove(num)
    else:
        flag = True
        num_pl_k = num
        while True:
            num_pl_k += k

            if num_pl_k in to_l:
                flag = True
                to_l.remove(num_pl_k)
                break
            if num_pl_k > max(to_l):
                break
if to_l:
    print(0)
else:
    print(1)
