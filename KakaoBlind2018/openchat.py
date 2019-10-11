def solution(record):
    dic = dict()  # key: ID, value: Nickname
    for r in record:
        rr = r.split()
        instruct = rr[0]
        identity = rr[1]
        if instruct != 'Leave':
            nickname = rr[2]
            dic[identity] = nickname

    answer = []
    for r in record:
        rr = r.split()
        instruct = rr[0]
        identity = rr[1]
        if instruct == 'Enter':
            answer.append(dic[identity] + "님이 들어왔습니다.")
        elif instruct == 'Leave':
            answer.append(dic[identity] + "님이 나갔습니다.")
    
    return answer


if __name__ == "__main__":
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    print(solution(record))
