t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    imp_list = list(map(int, input().split()))
    idx = list(range(len(imp_list)))
    idx[m] = 'print'

    s = 0
    while True:
        if imp_list[0] == max(imp_list):
            s += 1
            if idx[0] == 'print':
                print(s)
                break
            else:
                imp_list.pop(0)
                idx.pop(0)

        else:
            imp_list.append(imp_list.pop(0))
            idx.append(idx.pop(0))

