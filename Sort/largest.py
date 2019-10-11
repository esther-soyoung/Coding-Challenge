from collections import defaultdict

def solution(numbers):
    answer = ''
    nums = []  # list of string integers
    for n in numbers:
        nums.append(str(n))

    nums.sort(key = len, reverse = False)
    mysort(nums)
'''
    for i in [x for x in range(len(nums) - 1) if x % 2 == 0]:
        if nums[i][0] != nums[i+1][0]:
            answer += nums[i] + nums[i+1]
        else:  # When the first digits are equal
            tmp1 = nums[i] + nums[i+1]
            tmp2 = nums[i+1] + num[i]
            if tmp1 > tmp2:
                answer += nums[i]

    if int(answer) == 0:
        answer = '0'
    return answer
'''


''' Sort by the first digit.
    If tie, sort by second digit, so on.
'''
def mysort(lst):  # list of string integers
    lst.sort(reverse = True)
    dic = defaultdict(list)  # key: first digit
    for i in lst:
        dic[i[0]].append(i)

    for k, v in dic.items():
        v.sort(key = lambda x : x[1], reverse = True)



if __name__ == "__main__":
    numbers = [6, 10, 2]
    print(solution(numbers))  # 6210
    numbers = [3, 30, 34, 5, 9]
    print(solution(numbers))  # 9534330
