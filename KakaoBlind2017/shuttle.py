def solution(n, t, m, timetable):
    # initialize with the last bus time
    last_bus = 540 + t * (n-1)
    answer = time_to_str(last_bus)

    # sort timetable
    timetable_sort = [time_to_min(x) for x in timetable]
    timetable_sort.sort(reverse = False)

    # can take shuttle when both on time and on queue
    bus_time = 540  # initialize with the earliest bus
    on_bus = []  # crews who can take the bus
    for crew_time in timetable_sort:
        if crew_time > last_bus:  
            break
        if len(on_bus) == m or crew_time > bus_time:  # bus full or ttl
            on_bus.clear()  # bus takes off
            bus_time += t  # next bus
        on_bus.append(crew_time)

    # last group of crews to take bus
    if on_bus != []:
        if len(on_bus) < m:  # seats remaining
            answer = time_to_str(bus_time)
        elif len(on_bus) == m:   # be earlier than the last crew in group
            answer = time_to_str(on_bus[-1] - 1) 
    return answer


''' convert HH:MM to minutes
'''
def time_to_min(time_str):
    t = time_str.split(':')
    return 60 * int(t[0]) + int(t[1])


''' convert minutes to string of HH:MM
'''
def time_to_str(time_int):
    h = time_int // 60
    m = time_int - h * 60
    return format(h, '02.0f') + ':' + format(m, '02.0f')


if __name__ == "__main__":
    n = [1, 2, 2, 1, 1, 10]
    t = [1, 10, 1, 1, 1, 60]
    m = [5, 2, 2, 5, 1, 45]
    timetable = [["08:00", "08:01", "08:02", "08:03"], ["09:10", "09:09", "08:00"], ["09:00", "09:00", "09:00", "09:00"], ["00:01", "00:01", "00:01", "00:01", "00:01"], ["23:59"], ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]]

    for i in range(len(n)):
        print(solution(n[i], t[i], m[i], timetable[i]))
