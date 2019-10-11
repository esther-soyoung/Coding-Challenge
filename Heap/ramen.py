def solution(stock, dates, supplies, k):
    cnt = 0
    # Basecase
    if stock >= k:
        return cnt
    # import before stock runs out
    amt = 0
    date = 0

    z = list(zip(dates, supplies))


    for i in range(len(dates)):
        if dates[i] > stock:
            break
        else:
            if supplies[i] >= amt:
            	date = i
            	amt = supplies[i]
    dates.pop(date)
    supplies.pop(date)
    stock += amt
    cnt += 1
    cnt += solution(stock, dates, supplies, k)
    return cnt

if __name__ == '__main__':
    print(solution(4, [1, 2, 3, 4], [10, 40, 30, 20], 100))
