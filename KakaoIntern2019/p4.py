import bisect

def solution(k, room_number):
    answer = []
    occupied = []

    for r in room_number:
        assign(r, answer, occupied)
    return answer

    for r in room_number:
        i = 0
        while True:
            flag = assign(r + i, answer, occupied)
            if flag:
                break
            else:
                i += 1
    return answer


''' True if assigned
    else False
'''
def assign(r, answer, occupied):
    if r not in occupied:
        answer.append(r)
        bisect.insort(occupied,r)
    else:
        nxt = get_nxt(occupied)
        answer.append(nxt)
        bisect.insort(occupied, nxt)


def occupy(r, occupied):
    last = occupied[-1]
    if abs(r - last) > 1:

    
    
    

if __name__ == "__main__":
    k = 10
    room_num = [1,3,4,1,3,1]
    print(solution(k, room_num))
# [1,3,4,2,5,6]
