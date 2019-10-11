import heapq

def solution(stock, dates, supplies, k):
    ret = 0
    idx = 0
    h = []
    while (stock < k):
        for i in range(idx, len(dates)):
            if dates[i] <= stock:  # import
                heapq.heappush(h, (-supplies[i], supplies[i]))
                idx = i + 1
            else:
                break
        stock += heapq.heappop(h)[1]
        ret += 1
    return ret
