def solution(k, room_number):
    answer = []
    avail = []
    for i in range(len(room_number)):
        avail.append(-1 * (i + 1))

    for i in range(len(room_number)):
        r = room_number[i]
        if (-1 * r) in avail:
            answer.append(r)
            avail[r-1] = -1 * avail[r-1]
            continue
        avail = [o for o in avail if o < 0]
        for j in range(len(avail)):
            chck = avail[j]
            if (-1 * chck) > r:
                answer.append(-1 * chck)
                avail[j] = -1 * avail[j]
    return answer


if __name__ == "__main__":
    k = 10
    room_num = [1,3,4,1,3,1]
    print(solution(k, room_num))
# [1,3,4,2,5,6]
