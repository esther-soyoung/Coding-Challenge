def solution(s):
    sols = []  # length of compressed object for each i-unit

    for i in range(1, len(s) + 1):  # unit length i
        # list of sliced tokens of lenth i
        toks = []
        j = 0
        while j + i <= len(s): 
            toks.append(s[j : j+i])
            j += i
        if j + i != len(s):  # the rest
            toks.append(s[j:])
        
        # compress
        compressed = ''
        cnt = 1
        for j in range(len(toks) - 1):
            if toks[j] == toks[j+1]:  # compress
                cnt += 1
            else:  # stop compressing
                if cnt != 1:
                    compressed += str(cnt) + toks[j]
                else:
                    compressed += toks[j]
                cnt = 1  # reset count
        if cnt == 1:  # last token cannot be compressed
            compressed += toks[-1]
        else:  # compress last few tokens
            compressed += str(cnt) + toks[-1]
    
        sols.append(len(compressed))
    answer = min(sols)
    return answer


if __name__ == "__main__":
    s1 = 'aabbaccc'
    s2 = 'ababcdcdababcdcd'
    s3 = 'abcabcdede'
    s4 = 'abcabcabcabcdededededede'
    s5 = 'xababcdcdababcdcd'

    lst = [s1, s2, s3, s4, s5]
    for i in lst:
        print(solution(i))  # 7 9 8 14 17
