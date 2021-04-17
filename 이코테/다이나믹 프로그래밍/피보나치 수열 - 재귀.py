# 피보나치 함수 (Fibonacci Function)
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)


print(fibo(4))

# 단순 재귀 함수로 피보나치 수열을 해결하면 지수 시간 복잡도를 가지게 된다.
# 다음과 같이 f(2)가 여러 번 호출되는 것을 확인 할 수 있다. (중복되는 문졔)
# ex) f(6) = f(5) + f(4) = f(4) + f(3) + f(2) = f(3) + f(2) + f(2) + f(1) + f(2)
#       = f(2) + f(1) + f(2) + f(2) + f(1) + f(2)
