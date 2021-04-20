# 런타임 에러
# eval함수는 0으로 시작하는 수 입력 불가 - 런타임 에러
expr = input().split('-')
res = int(eval(expr[0]))
for i in range(1, len(expr)):
    res -= int(eval(expr[i]))
print(res)