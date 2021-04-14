from itertools import combinations_with_replacement

data = ['A', 'B', 'C']
res = list(combinations_with_replacement(data, 2))  # 2개를 뽑는 모든 조합 구하기 (중복 허용)
print(res)

# 출력 : [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
