def solution(heights):
    received = False
    ret = []
    for i in range(len(heights)):
        for j in reversed(range(i)):
        	# signal received
            if heights[j] > heights[i]:
                ret.append(j + 1)
                received = True
                break
     	# signal lost
        if not received:
        	ret.append(0)
        received = False
    return ret
