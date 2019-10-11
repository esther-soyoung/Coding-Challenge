def solution(arrangement):
    stack = list(arrangement)
    stick = 0
    answer = 0
    laser = True
    
    while len(stack) != 0:
        i = stack.pop()
        
        if i == '(':
            # laser
            if laser:
            	laser = False
            	stick -= 1
            	answer += stick
            # end of stick
            else:
                answer += 1
                stick -= 1
        else:
            laser = True
            stick += 1
    return answer
