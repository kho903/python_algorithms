def solution(s):
    answer = True
    stack = []
    sL = list(s)
    print(sL)
    for a in sL:
        if a == '(':
            stack.append(a)
        elif a == ')':
            if not stack or stack[-1]== ')':
                return False
            else:
                stack.pop()
    if stack:
        return False
    else:
        return True



print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))