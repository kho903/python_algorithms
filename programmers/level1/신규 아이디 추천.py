def first(new_id):
    res = ''
    for c in new_id:
        if c.isupper():
            res += c.lower()
        else:
            res += c
    return res


def second(id):
    res = ''
    for c in id:
        if 97 <= ord(c) <= 122 or c == '-' or c == '_' or c == '.' or 48 <= ord(c) <= 57:
            res += c
    return res


def third(id):
    res = []
    for c in id:
        if res:
            if c == '.' and res[-1] == '.':
                continue
        res += c
    return res


def forth(id):
    id = list(id)
    if id and id[0] == '.':
        id = id[1:]
    if id and id[-1] == '.':
        id = id[: -1]
    return id


def fifth(id):
    if not id:
        id.append("a")
    return id


def sixth(id):
    if len(id) >= 16:
        id = id[:15]
        if id[-1] == '.':
            id.pop()
    return id


def seventh(id):
    if len(id) <= 2:
        while len(id) <= 3:
            id += id[-1]
        return id[:3]
    else:
        return id


def solution(new_id):
    func_list = [first, second, third, forth, fifth, sixth, seventh]
    ans = new_id
    for f in range(7):
        ans = func_list[f](ans)
    return "".join(ans)


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
