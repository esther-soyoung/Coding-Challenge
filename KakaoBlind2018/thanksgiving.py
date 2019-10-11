def solution(lines):
    log = []
    for l in lines:
        log.append(start_end(l))
    log.sort(key = lambda x: x[0], reverse = False)
    return one_sec(log)
    

''' Get starting time and transform into seconds
    Input: String of log
    Return: Tuple (start_time, end_time) in seconds
'''
def start_end(log_string):
    s = log_string.split(' ')
    end = s[1]
    process = float(s[2][:-1])
    h, m, s = end.split(':')
    end_ = float(h) * 60 * 60 + float(m) * 60 + float(s)
    start_ = format(end_ - process + 0.001, '.3f')
    end_ = format(end_, '.3f')
    return (start_, end_)


''' Return the status of each process at the given time
    Input: start and end time of process, starting point of search window
    Return: String of status, 'On' or 'Yet' or 'Past'
'''
def status(start, end, t):
    fr = t  # starting point of search window
    to = float(format(t + 1 - 0.001, '.3f'))  # ending point of window
    # processes that start during search window
    if fr <= start and start <= to:
        return 'On'
    # processes that end during search window 
    elif fr <= end and end <= to:
        return 'On'
    # processes that start before window and end after window
    elif start < fr and end > to:
        return 'On'
    # processes that start after window: Yet to come
    elif to < start:
        return 'Yet'
    # processes that already ended before window: Past processes
    elif end < to:
        return 'Past'


''' Get the max number of processes processed within window of 1-sec.
    Examine both starting point and ending point of each process.
    Window size: 1 second
    Input: list of processes in tuples (start_time, end_time)
    Return: max number of processes at any time with window size 1 sec
'''
def one_sec(lst):
    max_process = []  # number of processes per window
    process_num = 0
    # examine each window
    for i in range(len(lst)):
        pivot = float(lst[i][0])  # start each window from starting time of each process
        # examine each process: within window or not
        for j in range(i, len(lst)):
            s = status(float(lst[j][0]), float(lst[j][1]), pivot)
            if s == 'On':
                process_num += 1
            elif s == 'Yet':
                break
        max_process.append(process_num)
        process_num = 0

        pivot = float(lst[i][1])  # start each window from ending time of each process
        # examine each process: within window or not
        for j in range(i, len(lst)):
            s = status(float(lst[j][0]), float(lst[j][1]), pivot)
            if s == 'On':
                process_num += 1
            elif s == 'Yet':
                break
        max_process.append(process_num)
        process_num = 0

    return max(max_process)
    

if __name__ == "__main__":
    inp = ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
    print(solution(inp))
