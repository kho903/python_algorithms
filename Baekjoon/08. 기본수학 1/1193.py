input_num = int(input())
first = 1
n = 1
plus_v = 2
if input_num == 1:
    print("1/1")
elif input_num == 2:
    print("1/2")
else:
    while True:
        n += 1
        if n % 2 == 1:
            first += plus_v
            plus_v += 4
            if (input_num >= first) and (input_num < first + int(plus_v / 2)):
                dif = input_num - first
                print(str(n - dif) + "/" + str(dif + 1))
                break
        else:
            first += 1
            if (input_num <= first) and (input_num >= first - int(plus_v)):
                dif = first - input_num
                print(str(n - dif) + "/" + str(dif - 1))
                break
