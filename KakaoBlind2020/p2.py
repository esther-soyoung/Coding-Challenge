def solution(p):
    if p == '':
        return p

    # split into u and v
    u = ''
    v = ''
    s_cnt = 0
    e_cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            s_cnt += 1
        else:
            e_cnt += 1
        u += p[i]
        i += 1
        if s_cnt == e_cnt:
            break
    if i < len(p): 
        v += p[i:]

    if valid(u):  # u is valid
        u += solution(v)
        return u
    else:  # u is not valid
        tmp = '(' + solution(v) + ')'
        u = u[1:-1]
        for i in u:
            if i == '(':
                tmp += ')'
            else:
                tmp += '('
        return tmp


def valid(u):
    cnt = 0
    for i in u:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    return cnt == 0


if __name__ == "__main__":
    p1 = '(()())()'  # "(()())()"
    p2 = ')('  # "()"
    p3 = '()))((()'  # "()(())()"
    lst = [p1, p2, p3]
    for l in lst:
        print(solution(l))

