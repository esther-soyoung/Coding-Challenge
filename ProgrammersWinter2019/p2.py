# Solutino using DP
def solution(n):
    answer = dict()
    answer[1] = [0]
    for i in range(2, n+1):
        print('for i: ', i)
        answer[i] = answer[i-1].copy()
        answer[i].append(0)
        print("answer[i-1]: ", answer[i-1])
        answer[i].extend(rev_con(answer[i-1]))
    return answer[n]

# Reverse and converse given list
def rev_con(lst):
    ret = []
    lst.reverse()
    for l in lst:
        ret.append(1-l)
    print(ret)
    return ret


if __name__ == "__main__":
    print(solution(2))
