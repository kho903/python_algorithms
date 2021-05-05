while True:
    n = input()
    if int(n) == 0:
        break
    i = 0
    i_back = len(n) - 1
    while i < i_back:
        if n[i] != n[i_back]:
            print("no")
            break
        i += 1
        i_back -= 1
    if i >= i_back:
        print("yes")
