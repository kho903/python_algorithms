n, m = map(int, input().split())
cards = list(map(int, input().split()))

for _ in range(m):
    if cards[0] > cards[1]:
        min_v = cards[0]
        min2_v = cards[1]
    else:
        min2_v = cards[0]
        min_v = cards[1]

    min_i, min2_i = cards.index(min_v), cards.index(min2_v)

    for i in range(2, n):
        if min2_v > cards[i]:
            if min_v > cards[i]:
                min2_v, min_v = min_v, cards[i]
                min2_i, min_i = min_i, i
            else:
                min2_v = cards[i]
                min2_i = i
    sum_min = min2_v + min_v
    cards[min_i], cards[min2_i] = sum_min, sum_min

print(sum(cards))
