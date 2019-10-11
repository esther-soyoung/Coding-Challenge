import re
from collections import deque

def solution(str1, str2):
    lst1 = ngram(str1, 2)
    lst2 = ngram(str2, 2)
    return jaccard(lst1, lst2)


''' Get ngrams of given string
    Input: string s, int n for n-gram
    Return: list of ngrams
'''
def ngram(s, n):
    q = deque(s)
    lst = []  # list of 2-grams before normalizing
    ret = []  # final list of 2-grams after normalizing
    a = q.popleft()
    # get 2-grams
    while q:
        tmp = a
        a = q.popleft()
        tmp += a  # 2-gram
        lst.append(tmp)
    # normalize
    for r in lst:
        r = normalize(r)
        if len(r) == 2:
            ret.append(r)
    return ret


''' Take only alphabets
    Transform into lowercase
    Input: string
    Return: normalized string
'''
def normalize(string):
    normed = re.sub("[^a-zA-Z]", '', string)
    normed = re.sub("^ | $", '', normed)
    normed = normed.lower()
    return normed


''' intersection
    allowing repeated elements
    Input: two lists to intersect
    Return: list of intersection elements, including repetition
'''
def intersection(lst1, lst2):
    lst1 = lst1.copy()
    lst2 = lst2.copy()
    inter = []
    while lst1:
        a = lst1.pop()
        if a in lst2:
            lst2.remove(a)
            inter.append(a)
    return inter


''' Get Jaccard Coefficient
    Input: two lists to compute Jaccard Coefficient on
    Return: integer part of JC after multiplying by 65536
'''
def jaccard(lst1, lst2):
    inter = intersection(lst1, lst2)
    try:
        jac = len(inter) / (len(lst1) + len(lst2) - len(inter))
    except ZeroDivisionError:
        jac = 1  # 1 when empty
    jac = jac * 65536
    return int(jac)


if __name__ == "__main__":
    print(solution('FRANCE', 'french'))  # 16384
    print(solution('handshake', 'shake hands'))  # 65536
    print(solution('aa1+aa2', 'AAAA12'))  # 43690
    print(solution('E=M*C^2', 'e=m*c*^2'))  # 65536
