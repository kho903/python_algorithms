s = input()
while True:
    if s[0:2] == "pi" or s[0:2] == "ka":
        s = s[2:]
        continue
    elif s[0:3] == "chu":
        s = s[3:]
        continue
    if len(s) == 0:
        print("YES")
        break
    elif len(s) != 0:
        print("NO")
        break
