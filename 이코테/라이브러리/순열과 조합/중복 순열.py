from itertools import product

data = ['A', 'B', 'C']
res = list(product(data, repeat=2))  # 2개를 뽑는 모든 순열 구하기 (중복 허용)
print(res)

# 출력 : [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
