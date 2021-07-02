def solution(dartResult):
    s = 0
    temp = []
    while True:
        n = int(dartResult[s])
        s += 1
        if n == 1 and dartResult[s] == '0':
            n = 10
            s += 1
        if dartResult[s] == 'S':
            temp.append(n)
        elif dartResult[s] == 'D':
            temp.append(n ** 2)
        elif dartResult[s] == 'T':
            temp.append(n ** 3)
        s += 1
        if s < len(dartResult):
            if dartResult[s] == '*':
                temp[-1] *= 2
                if len(temp) > 1:
                    temp[-2] *= 2
                s += 1
            elif dartResult[s] == '#':
                temp[-1] *= -1
                s += 1
        if s == len(dartResult):
            break
    # print(temp)
    return sum(temp)


print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))
