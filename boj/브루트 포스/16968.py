# def go(s, index, last):
#     if len(s) == index:
#         return 1
#     start = ord('a') if s[index] == 'c' else ord('0')
#     end = ord('z') if s[index] == 'c' else ord('9')
#     ans = 0
#     for i in range(start, end + 1):
#         if i != last:
#             ans += go(s, index + 1, i)
#     return ans
#
#
# s = input()
# print(go(s, 0, ' '))


s = input()
ans = 1
for i in range(len(s)):
    if s[i] == 'c':
        cnt = 26
    else:
        cnt = 10
    if i > 0 and s[i] == s[i - 1]:
        cnt -= 1
    ans *= cnt

print(ans)
