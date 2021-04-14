# 순열 : 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것
#  - {'A', 'B', 'C'} 에서 3개를 선택하여 나열하는 경우
# 'ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'

from itertools import permutations

data = ['A', 'B', 'C']

res = list(permutations(data, 3))  # 모든 순열 구하기
print(res)

# 출력 : [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
