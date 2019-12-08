import sys

def solution(triangle):
    M = [triangle[0]]
    for i in range(1, len(triangle)):
        tmp = []
        # handle the first element
        tmp.append(M[i-1][0] + triangle[i][0])
        # handle the body elements
        for j in range(1, len(triangle[i]) - 1):
            tmp.append(max(M[i-1][j], M[i-1][j-1]) + triangle[i][j]) 
        # handle the last element
        j = len(triangle[i]) - 1
        tmp.append(M[i-1][j-1] + triangle[i][j])
        M.append(tmp)

    return max(M[-1])

if __name__ == "__main__":
    tri = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    print(solution(tri))  # 30

    

