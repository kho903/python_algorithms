from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])  # 'blue'가 등장한 횟수 출력
print(counter['green'])  # 'green'가 등장한 횟수 출력
print(dict(counter))

# 출력 결과
# 3
# 1
# {'red': 2, 'blue': 3, 'green': 1}
