# # 내가 푼 방법
# n = input()
# m = int(input())
# btn = list(input().split())
# res = []
# count = 0
# if n == '100':
#     print(0)
# else:
#     for i in n:
#         if i not in btn:
#             count += 1
#             res.append(i)
#         else:
#             a = 1
#             res.append([])
#             t = 0
#             count += 1
#             while True:
#                 if str(int(i) - a) not in btn and int(i) - a >= 0:
#                     res[-1].append(str(int(i) - a))
#                     t = 1
#                 if str(int(i) + a) not in btn:
#                     res[-1].append(str(int(i) + a))
#                     t = 1
#                 if t == 1:
#                     break
#                 a += 1
#     a = ''
#     b = ''
#     for i in range(len(res)):
#         a += res[i][0]
#         b += res[i][-1]
#     a = int(a)
#     b = int(b)
#     if abs(a - int(n)) <= abs(b - int(n)):
#         p = abs(a - int(n))
#     else:
#         p = abs(b - int(n))
#     if abs(int(n) - 100) > count + p:
#         print(count + p)
#     else:
#         print(abs(int(n) - 100))

# # 인터넷 참고
import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
btn = list(input().split())
res = abs(n - 100)
for i in range(1000001):
    num = list(str(i))
    t = True
    for j in num:
        if j in btn:
            t = False
            break
    if t:
        res = min(res, len(str(i)) + abs(i - n))
print(res)
