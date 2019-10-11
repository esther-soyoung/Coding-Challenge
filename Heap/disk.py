# Build a priority queue with currently available jobs.
# Shortest jobs first.

import heapq

def solution(jobs):
    jobs.sort()
    curr = 0
    total = 0

    num_jobs = len(jobs)
    for i in range(num_jobs):
        j = get_job(curr, jobs)  #(req time, opr time)

        if j[0] <= curr:  # start rightaway
            total += j[1] + curr - j[0]  # opr time + wait time
            curr += j[1]
        else:  # intermission between jobs
            total += j[1]
            curr = j[0] + j[1]

    return int(total / num_jobs)


''' Return job which is
    requested before current time and
    takes shortest operation time.
'''
def get_job(curr, jobs):
    jobs_req = jobs.copy()
    heapq.heapify(jobs_req)

     # jobs requested before current time
    jobs_avail = []  # [(request, operation)] 
    for j in jobs_req:
        if j[0] > curr:
            break
        jobs_avail.append(j)

    if not jobs_avail:  # no job requested while operating
        j = heapq.heappop(jobs_req)  # job requested first
        jobs_avail.append(j)
        for j_ in jobs_req:  # append all jobs with same req time
            if j_[0] > j[0]:
                break
            jobs_avail.append(j_)

    jobs_avail = [[i[1], i[0]] for i in jobs_avail]  # sort by opr time
    heapq.heapify(jobs_avail)

    tmp = heapq.heappop(jobs_avail)  # (opr time, req time)
    ret = [tmp[1], tmp[0]]  # (req time, opr time)

    # remove the job from the jobs list
    jobs.remove(ret)
    return ret


if __name__ == '__main__':
    jobs = [[0, 3], [1, 9], [2, 6], [4, 3]]
    print(solution(jobs))  # 6
