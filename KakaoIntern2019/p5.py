def solution(stones, k):
    answer = 0
    while True:
        kk = 0
        for s in range(len(stones)):
            if stones[s] > 0:
                stones[s] -= 1
            else:
                if s > 0 and stones[s-1] != 0:
                    kk = 0
                kk += 1
                if kk > k:
                    return answer
        answer += 1
    return answer


if __name__ == "__main__":
    stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
    k = 3
    print(solution(stones, k))
# 3
