n, m = map(int, input().split())
card = list(map(int, input().split()))
sum_card = []
for i in range(len(card) - 2):
    for j in range(i + 1, len(card) - 1):
        for k in range(j + 1, len(card)):
            sum_card.append(card[i] + card[j] + card[k])

sum_card = sorted(list(set(sum_card)))

for i in range(len(sum_card) - 1, 0, -1):
    if sum_card[i] <= m:
        print(sum_card[i])
        break
