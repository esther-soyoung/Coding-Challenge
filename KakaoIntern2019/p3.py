from collections import defaultdict

def solution(user_id, banned_id):
    answer = 1
    dic = defaultdict(list)

    for b in banned_id:
        for u in user_id:
            if len(u) != len(b):
                continue
            if match(u, b):
                dic[b].append(u)            

    if len(dic) == 0:
        return 0
    
    cnt = []
    for k, v in dic.items():
        if banned_id.count(k) != len(v):
            cnt.append(v)

    for i in range(len(cnt)):
        

            

    return answer


'''return boolean
'''
def match(u, b):
    for i in range(len(u)):
        if b[i] == '*':
            continue
        if b[i] != u[i]:
            return False
    return True


if __name__ == "__main__":
    uid = [["frodo", "fradi", "crodo", "abc123", "frodoc"], ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["frodo", "fradi", "crodo", "abc123", "frodoc"]]
    bid = [["fr*d*", "abc1**"], ["*rodo", "*rodo", "******"], ["fr*d*", "*rodo", "******", "******"]]

    for i in range(len(uid)):
        print(solution(uid[i], bid[i]))



'''
2
2
3
'''
