k = int(input())
bin_k = str(bin(k + 1))[3:]
for i in range(len(bin_k)):
    if bin_k[i] == '0':
        print(4, end='')
    elif bin_k[i] == '1':
        print(7, end='')
# 4, 7

# 4
# 7
# 44
# 47
# 74
# 77
# 444
# 447
# 474
# 477
# 744
# 747
# 774
# 777
# 4444
# 4447
# 4474
# 4477
# 4744
# 4747
# 4774
# 4777
