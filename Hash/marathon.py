def solution(p, c):
    p.sort()
    c.sort()
    c.append(0)
    for i in range(len(p)):
        if p[i] != c[i]:
            return p[i]
