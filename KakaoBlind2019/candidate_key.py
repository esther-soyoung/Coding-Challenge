import itertools
import sys

def solution(relation):
    answer = 0
    cols = [i for i in range(len(relation))]
    for c in cols:
        if unique(relation, [c]):
            answer += 1
            cols.remove(c)
    i = 2
    while cols:
        cand_key = combination(cols, i)
        if cand_key is None:
            return answer
        if unique(relation, cand_key):
            answer += 1
            for c in cand_key:
                cols.remove(c)
        i += 1
    return answer


''' Return possible combinations of elements in cols list
    of size num
    Input: 
    cols: list to get combinations from
    num: size of combinations
    Return: list of all the possible combinations
    Return None if num > len(cols)
'''
def combination(cols, num):
    if num > len(cols):
        return None
    return list(itertools.combinations(cols, num)) 


''' Check uniqueness of candidate key
    Input: list of column indices of candidate key
    candidate key as list ex)['ryan', 'music']
    Output: Boolean
'''
def unique(relation, cand_key):
    uniq = set()
    for r in relation:
        if tuple([r[i] for i in cand_key]) in uniq:
            return False
        uniq.add(tuple([r[i] for i in cand_key]))
    return True


if __name__ == "__main__":
    relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
    print(solution(relation))  # 2
