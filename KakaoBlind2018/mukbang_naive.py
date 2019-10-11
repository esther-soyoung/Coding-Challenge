def solution(food_times, k):
    done = 0
    sec = -1
    if k >= sum(food_times):
        return -1
    while True:
        for i in range(len(food_times)):
            if food_times[i] == 0:
                continue
            food_times[i] -= 1  # consume
            sec += 1
            if sec == k:
                return (i + 1)
