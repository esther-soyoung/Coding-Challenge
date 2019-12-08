import re
from collections import deque

def solution(s):
    s = s[1:-1]
    # single item
    if s.count('{') == 1:
        ret = []
        s = s[1:-1]
        ret.append(int(s))
        return ret

    answer = []
    tups = get(s)
    tups.sort(key = lambda x : len(x))

    for t in tups:
        for i in t:
            answer.append(i)

    ret = []
    while answer:
        popped = answer.pop(0)
        ret.append(popped)
        answer = [i for i in answer if i != popped]

    return ret


''' list of tuples
    each tuple as a list of natural numbers
    input: '{1,2,3},{2,1},{1,2,4,3},{2}'
    output: [[1, 2, 3], [2, 1], [1, 2, 4, 3], [2]]
'''
def get(s):
    ret = []
    p = re.compile('{(.+?)}')
    m = p.findall(s)
    for t in m:
        tmp = []
        if t.count(',') == 0:
            tmp.append(int(t))
            ret.append(tmp)
            continue
        elm = t.split(',')
        for i in elm:
            tmp.append(int(i))
        ret.append(tmp)
    return ret


if __name__ == "__main__":
    ss = ["{{2},{2,1},{2,1,3},{2,1,3,4}}", "{{1,2,3},{2,1},{1,2,4,3},{2}}", "{{20,111},{111}}", "{{123}}", "{{4,2,3},{3},{2,3,4,1},{2,3}}"]
    for s in ss:
        print(solution(s))

'''
[2, 1, 3, 4]
[2, 1, 3, 4]
[111, 20]
[123]
[3, 2, 4, 1]
'''
