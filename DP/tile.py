def solution(N):
    if N == 1:
        return 4
    M = fib_dp(N)
    N = N-1
    return 2 * (M[N] + M[N-1] + M[N])

def fib(n):
    if (n == 0) or (n == 1):
        return 1
    return fib(n-1) + fib(n-2)

def fib_dp(n):
    M = [1, 1]
    for i in range(2, n):
        M.append(M[i-1] + M[i-2])
    return M


if __name__ == "__main__":
    N = [5, 6]
    for n in N:
        print(solution(n))  # 26, 42
