from collections import Counter

def solution(N, stages):
    answer = []  # [(stage_num, failure rate)]
    c = Counter(stages)
    for i in range(1, N+1):
        on_stage = c[i]
        on_clear_stage = on_or_cleared(i, N, c)
        if on_clear_stage == 0:
            answer.append((i, 0))
        else:
            answer.append((i, on_stage / on_clear_stage))
    
    # sort
    answer.sort(key = lambda x: x[1], reverse = True)
    answer = [i[0] for i in answer]
    return answer


''' Return the number of players who
    are currently on the stage or
    already cleared the stage

    stage_num: stage number to look at
    N: number of total stages
    counter_stages: counter object on list stages
'''
def on_or_cleared(stage_num, N, counter_stages):
    ret = 0
    for i in range(stage_num, N + 2):
        ret += counter_stages[i]
    return ret


if __name__ == "__main__":
    N = [5, 4]
    stages = [[2, 1, 2, 6, 2, 4, 3, 3], [4,4,4,4,4]]
    for n in range(len(N)):
        print(solution(N[n], stages[n]))
    # [3,4,2,1,5]
    # [4,1,2,3]
