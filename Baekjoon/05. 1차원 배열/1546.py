n = int(input())
score = list(map(int, input().split()))
max_score = max(score)
res = 0
for i in range(n):
    res += score[i] * 100 / max_score

print(res / n)