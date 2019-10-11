import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while True:
        try:
            l = heapq.heappop(scoville)
            if l >= K:
                return cnt
            r = heapq.heappop(scoville)
            heapq.heappush(scoville, l + 2 * r)
            cnt += 1
        except:
            return -1
