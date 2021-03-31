n = int(input())


def group_word_check(w):
    for i in range(len(w) - 2):
        for j in range(i + 1, len(w) - 1):
            if w[i] == w[j]:
                pass
            elif w[i] != w[j]:
                j += 1
                if w[i] == w[j]:
                    return False
    return True


count = 0
for i in range(n):
    word = input()
    if group_word_check(word):
        count += 1

print(count)
