def solution(pb):
    pb.sort()
    for i in range(len(pb) - 1):
        if pb[i] == pb[i+1][:len(pb[i])]:
            return False
    return True
