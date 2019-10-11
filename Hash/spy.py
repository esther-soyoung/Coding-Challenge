from collections import defaultdict
def solution(clothes):
    dic = defaultdict(list)
    for c in clothes:
        dic[c[1]].append(c[0])
    answer = 0
    temp1 = 1
    temp2 = 0
    for key, val in dic.items():
        j = len(val) * (temp1 + temp2)
        answer += j
        temp1 = temp1 + temp2
        temp2 = j
    return answer
