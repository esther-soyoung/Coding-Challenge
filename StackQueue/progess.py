import math

def solution(progresses, speeds):
    release = []
    ret = []
    
    for i in range(len(progresses)):
        left = 100 - progresses[i]
        days = math.ceil(left / speeds[i])
        release.append(days)
        
    for i in range(len(release)):
        if release[i] < 0:
            continue
        cnt = 1
        for j in range(i + 1, len(release)):
            if release[j] < 0:
                continue
            if release[j] > release[i]:
                break
            else:
                cnt += 1
                release[j] = -1
        ret.append(cnt)
    return ret
