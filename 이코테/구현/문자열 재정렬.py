# 내가 푼 방법
# s = list(input())
# str_s = []
# sum_s = 0
# for i in range(len(s)):
#     if '0' > s[i] or s[i] > '9':
#         str_s.append(s[i])
#     else:
#         sum_s += int(s[i])
# str_s.sort()
# for i in range(len(str_s)):
#     print(str_s[i], end='')
# print(sum_s)

data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력 (리스트를 문자열로 변환하여 출력
print(''.join(result))
