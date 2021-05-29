def check(password):
    ja = 0
    mo = 0
    for p in password:
        if p in "aeiou":
            mo += 1
        else:
            ja += 1
    return ja >= 2 and mo >= 1


def make_pw(n, alpha, password, i):
    if len(password) == n:
        if check(password):
            print(password)
        return
    if i == len(alpha):
        return
    make_pw(n, alpha, password + alpha[i], i + 1)
    make_pw(n, alpha, password, i + 1)


n, m = map(int, input().split())
arr = input().split()
arr.sort()
make_pw(n, arr, "", 0)
