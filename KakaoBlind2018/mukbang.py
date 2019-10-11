def solution(food_times, k):
    if k >= sum(food_times):
        return -1
    
    num_food = len(food_times)
    num_rotate = k // num_food
    rest = k % num_food

    food_left = list(map(lambda x : x - num_rotate, food_times))
    for i in range(num_food):
        if food_left[i] < 0:
            rest -= food_left[i]
            food_left[i] = 0

    for j in range(num_food):
        if food_left[j] != 0:
            rest -= 1
        if rest == 0:
            return (j + 2) % num_food


if __name__ == "__main__":
    food_times = [3, 1, 2]
    k = 5
    print(solution(food_times, k))
    food_times = [5, 3, 1, 2]
    k = 8
    print(solution(food_times, k))
