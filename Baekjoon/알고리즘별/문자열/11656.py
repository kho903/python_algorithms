n = input()
sfx = []
for i in range(len(n)):
    sfx.append(n[i:len(n)])

sfx.sort()
for a in sfx:
    print(a)