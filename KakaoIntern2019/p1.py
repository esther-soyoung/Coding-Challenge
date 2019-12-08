import sys

def solution(board, moves):
    answer = 0
    moves = [i - 1 for i in moves]
    basket = []

    for m in moves:
        item = pick(board, m)
        if item != -1:
            basket.append(item)

    while True:
        num = pop(basket)
        if num == 0:
            break
        answer += num
    return answer


''' return -1 if nothing to pick
'''
def pick(board, m):
    for i in range(len(board)):
        if board[i][m] == 0:
            continue
        item = board[i][m]
        board[i][m] = 0
        return item
    return -1


def pop(basket):
    pop = []
    for i in range(len(basket) - 1):
        if basket[i] == 0:
            continue
        if basket[i] == basket[i + 1]:
            pop.append(i)
            pop.append(i+1)
    if len(pop) != 0:
        for p in range(len(pop)):
            basket.pop(pop[p]-p)
    return len(pop)


if __name__ == "__main__":
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]
    print(solution(board, moves))  # 4
