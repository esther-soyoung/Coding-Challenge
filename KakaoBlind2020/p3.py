def solution(key, lock):
    M = len(key)
    N = len(lock)
    # Get the coordinates of holes in lock
    holes = []
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                holes.append((i, j))
    # Get the coordinates of bumps in key
    bumps = []
    for i in range(M):
        for j in range(M):
            if key[i][j] == 1:
                bumps.append((i, j))

    # Not enough number of bumps
    if len(bumps) < len(holes):
        return False
    # No holes. Key should have no bumps
    if len(holes) == 0:
        if len(bumps) == 0:
            return True
        return False
    # All holes. Key should have all bumps
    if len(holes) == N * N:
        if len(bumps) == N * N:
            return True
        return False

    # Naive check
    if check(bumps, holes, N):
        return True

    # Rotate and Check
    i = 0
    while i < 3:
        bumps = rotate(bumps, M)
        i += 1
        if check(bumps, holes, N):
            return True

    return False


''' Check if bumps can fill all the holes
'''
def check(bumps, holes, N):
    #print('checking')
    bumps.sort(key = lambda x : (x[0], x[1]))
    holes.sort(key = lambda x : (x[0], x[1]))

    # Check relative locations (Move key)
    # for each pivot bump,
    pivot_match = 0
    gaps = ()
    for b in bumps:  # pivot bump
        bumps_rest = bumps.copy()
        bumps_rest.remove(b)
        extra = bumps_rest.copy()
        gaps = (holes[0][0] - b[0], holes[0][1] - b[1])

        for i in range(1, len(holes)):
            h_x, h_y = holes[i]
            for r in bumps_rest:
                g_x = h_x - r[0]
                g_y = h_y - r[1]
                if (g_x == gaps[0]) and (g_y == gaps[1]):  # matching bump for holes[i]
                    pivot_match += 1
                    extra.remove(r)
                    break  # move on to next hole
            if pivot_match < i:  # hole doesn't have matching bump
                break  # wrong pivot bump

        if pivot_match != (len(holes) - 1):
            continue  # wrong pivot bump

        # Check surroundings
        if extra == []:  # No extra bumps
            #print('True: no extra')
            return True  # No need to check surroundings

        conflict = False
        for e in extra:
            rel_loc = (e[0] + gaps[0], e[1] + gaps[1])
            # Conflicting bumps
            if rel_loc[0] < N and rel_loc[1] < N:
                conflict = True
                break  # move on to next pivot bump

        # Clean
        if not conflict:
            #print('True: no conflicts')
            return True
                

''' Rotate the points in given matrix for 90 degrees
'''
def rotate(bumps, M):
    r90 = []
    for x, y in bumps:
        x_ = y
        y_ = (M - 1) - x
        r90.append((x_, y_))
    return r90


if __name__ == "__main__":
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print(solution(key, lock))  # True
    key = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
    print(solution(key, lock))  # False
