from collections import deque

def solution(cacheSize, cities):
    answer = 0
    # empty cache
    if cacheSize == 0:
        return 5 * len(cities)
    # large cache
    if cacheSize > len(cities):
        return len(cities)

    cache = deque()
    for i in range(len(cities)):
        # cache hit
        if cities[i].lower() in cache:
            answer += 1
            # update cache
            cache.remove(cities[i].lower())
            cache.append(cities[i].lower())
        # cache miss
        else:
            answer += 5
            cache.append(cities[i].lower())
            # initialize cache
            if len(cache) <= cacheSize:
                continue
            # update cache
            else:
                cache.popleft()
    return answer



if __name__ == "__main__":
    cacheSize = 3
    cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
    print(solution(cacheSize, cities))
