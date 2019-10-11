def solution(priorities, location):
    ret = location
    while True:
        for i in range(len(priorities)):
            # target job
            if i == location:
                # print
                if priorities[i] >= max(priorities[:i] + priorities[i+1:]):
                    return ret + 1
                # to the end
                else:
                    ret = len(priorities) - 1
            # not the target job
            else:
                # print
                if priorities[i] >= max(priorities[:i] + priorities[i+1:]):
                    priorities[i] = -1
                    continue
                # already printed
                elif priorities[i] == -1:
                    continue
                # to the end
                else:
                    ret -= 1
