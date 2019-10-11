''' Maintain min-heap and max-heap.
    Insert and Delete from both queues.
    Multiply -1 when inserting to max heap.
'''

import sys
import heapq

def solution(operations):
    heap = []

    for i in operations:
        opr = i.split(' ')
        if opr[0] == 'I':
            heapq.heappush(heap, int(opr[1]))
#            heapq.heappush(heap, (i[2], -1 * i[2]))
        elif opr[0] == 'D':
            if opr[1] == '1':  #  Delete max element
                ret = heapq.nlargest(1, heap)
                for i in ret:
                    heap.remove(i)
            if opr[1] == '-1':  # Delete min element
                ret = heapq.nsmallest(1, heap)
                for i in ret:
                    heap.remove(i)
        else:
            sys.exit("Invalid operation")

    if not heap:
        answer = [0, 0]
    else:
        [max_] = heapq.nlargest(1, heap)
        [min_] = heapq.nsmallest(1, heap)
        answer = [max_, min_]
    return answer


if __name__ == "__main__":
    operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
    print(solution(operations))  # [333, -45]

