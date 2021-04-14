# 조합
# - 서로 다른 n개에서 순서에 상관 없이 서로 다른 r개를 선택하는 것
# {'A', 'B', 'C'} 에서 순서를 고려하지 않고 두개를 뽑는 경우 : 'AB', 'AC', 'BC'
from itertools import combinations

data = ['A', 'B', 'C']  # 데이터 준비

res = list(combinations(data, 2))  # 2개를 뽑는 모든 조합 구하기
print(res)

# 출력 : [('A', 'B'), ('A', 'C'), ('B', 'C')]
