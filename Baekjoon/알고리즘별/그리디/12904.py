s = input()
t = input()
s_d = [s]

while True:
    for i in range(len(s_d)):
        s_d.append(s_d[i] + 'A')
        s_d.append(s_d[i][::-1] + 'B')
    if t in s_d:
        print(1)
        break
    if len(s_d[-1]) >= len(t):
        print(0)
        break
