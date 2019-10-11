from collections import deque

def solution(m, n, board):
    board = [list(b) for b in board]
    answer = 0
    while True:
        num, board = block_pop(m, n, board)
        if num == 0:
            break
        answer += num
    return answer


''' Pop and drop adjacent four blocks
    Return False if nothing to pop
    Otherwise return True
'''
def block_pop(m, n, board):
    pop = set()
    for i in range(m - 1):
        for j in range(n - 1):
            if board[i][j] == 0:  # already popped
                continue
            if board[i][j] == board[i][j+1] and board[i][j] == board[i+1][j] and board[i+1][j] == board[i+1][j+1]:
                pop.update([(i, j), (i, j+1), (i+1, j), (i+1, j+1)])
    if len(pop) != 0:
        for p in pop:
            board[p[0]][p[1]] = 0
        board = cascade(m, n, board)
    return len(pop), board


''' Cascade all the popped blocks
    Return cascaded board
'''
def cascade(m, n, board):
    rotated = []
    for j in range(n):
        vertical = deque(board[i][j] for i in range(m))
        cnt = 0
        try:
            while True:
                vertical.remove(0)
                cnt += 1
        except ValueError:
            pass
        for i in range(cnt):
            vertical.appendleft(0)
        rotated.append(vertical)
    return [[rotated[j][i] for j in range(n)] for i in range(m)]


if __name__ == "__main__":
    m = [4, 6]
    n = [5, 6]
    board = [["CCBDE", "AAADE", "AAABF", "CCBBF"], ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]]
    for i in range(len(m)):
        print(solution(m[i], n[i], board[i]))  # 14, 15
