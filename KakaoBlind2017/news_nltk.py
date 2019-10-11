import re
from nltk.util import ngrams

def solution(str1, str2):
    lst1 = ngram(str1, 2)
    lst2 = ngram(str2, 2)
    return jaccard(lst1, lst2)


def ngram(s, n):
    lst = list(ngrams(s, n))
    ret = []
    for a, b in lst:
        l = a + b
        l = normalize(l)
        if len(l) == 2:
            ret.append(l)
    return ret


def normalize(string):
    normed = re.sub("[^a-zA-Z]", '', string)
    normed = re.sub("^ | $", '', normed)
    normed = normed.lower()
    return normed


def jaccard(lst1, lst2):
    inter = [i for i in lst1 if i in lst2]
    try:
        jac = len(inter) / (len(lst1) + len(lst2) - len(inter))
    except ZeroDivisionError:
        jac = 1
    jac = jac * 65536
    return int(jac)


if __name__ == "__main__":
    #print(solution('FRANCE', 'french'))  # 16384
    #print(solution('handshake', 'shake hands'))  # 65536
    #print(solution('aa1+aa2', 'AAAA12'))  # 43690
    print(solution('E=M*C^2', 'e=m*c*^2'))  # 65536
