

n, m = map(int, input().split())
n_l = []
m_l = []
for _ in range(n):
    n_l.append(input())

for _ in range(m):
    m_l.append(input())

nm = list(set(n_l) & set(m_l))

nm.sort()
print(len(nm))
for name in nm:
    print(name)
