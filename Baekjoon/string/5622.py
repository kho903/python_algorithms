def calc(a):
    sum_res = 0
    for i in a:
        sum_res += int((ord(i) - 65) / 3) + 3
        if i == 'S' or i == 'V' or i == 'Y' or i == 'Z':
            sum_res -= 1
    return sum_res


print(calc(input()))
