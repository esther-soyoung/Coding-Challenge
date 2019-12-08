def graph(land, height):
    N = len(land)
    edges = dict()
    
    for i in range(N-1):
        if (abs(land[i][0] - land[i+1][0]) <= height):
            edges[((i, 0), (i+1, 0))] = abs(land[i][0] - land[i+1][0])
        if (abs(land[i][N-1] - land[i+1][N-1]) <= height):
            edges[((i, N-1), (i+1, N-1))] = abs(land[i][N-1] - land[i+1][N-1])
        if (abs(land[i][0] - land[i][1]) <= height):
            edges[((i, 0), (i, 1))] = abs(land[i][0] - land[i][1])
        if (abs(land[i][N-2] - land[i][N-1]) <= height):
            edges[((i, N-2), (i, N-1))] = abs(land[i][N-2] - land[i][N-1])
                                           
    for j in range(N-1):
        if (abs(land[0][j] - land[0][j+1]) <= height):
            edges[((0, j), (0, j+1))] = abs(land[0][j] - land[0][j+1])
        if (abs(land[N-1][j] - land[N-1][j+1]) <= height):
            edges[((N-1, j), (N-1, j+1))] = abs(land[N-1][j] - land[N-1][j+1])
        if (abs(land[0][j] - land[1][j]) <= height):
            edges[((0, j), (1, j))] = abs(land[0][j] - land[1][j])
        if (abs(land[N-2][j] - land[N-1][j]) <= height):
            edges[((N-2, j), (N-1, j))] = abs(land[N-2][j] - land[N-1][j])
                                            
    for i in range(1, N-2):
        for j in range(1, N-2):
            if (abs(land[i][j] - land[i][j+1]) <= height):
                edges[((i, j), (i, j+1))] = abs(land[i][j] - land[i][j+1])
            if (abs(land[i][j] - land[i+1][j]) <= height):
                edges[((i, j), (i+1, j))] = abs(land[i][j] - land[i+1][j])
                                                
    return edges   

if __name__ == "__main__":
    land = [[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]]
    height = 3
    g = graph(land, height)
    if (3, 3) not in g:
        print(0)
