import sys

def solution(m, n, puddles):
    M = [[0]]
    for j in range(1, m):
        if [1, j+1] not in puddles:
            print(j)
            M[0].append(M[0][j-1] + 1)
        else:
            M[0].append(0)
    for i in range(1, n):
        if [i+1,  

    for i in range(2, n):
        for j in range(1, m):
            print(M)
            if [i, j] in puddles:
                M.append(0)
            else:
                print('[i-1][j]', i-1, ' ', j)
                print('[i][j-1]', i, ' ', j-1)
                sol = max(M[i-1][j], M[i][j-1])
                if sol != 0:
                    M.append(sol + 1)
                else:
                    M.append(0)
    return M[n-1][m-1]


if __name__ == "__main__":
    m = 4
    n = 3
    puddles = [[2, 2]]
    print(solution(m, n, puddles))  # 4

