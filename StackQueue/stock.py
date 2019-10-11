def solution(prices):
    ret = []
    fallen = False
    for i in range(len(prices)):
        sec = 0
        for j in range(i+1, len(prices)):
            sec += 1
            # stock price fallen
            if prices[j] < prices[i]:
                ret.append(sec)
                fallen = True
                break
        # stock price never fallen
        if not fallen:
            ret.append(sec)
        fallen = False
    return ret
