# For https://practice.geeksforgeeks.org/problems/shortest-path-from-1-to-n/0
for z in range(0, t):
    n = int(input())
    matrix = [[0 for i in range(0, n)] for j in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            if ((j+1) == (i+2)) or ((j+1) == 3*(i+1)):
                matrix[i][j] = 1
    
    
    visited = []
    distances = {}
    
    distances[1] = 0
    visited.append(1)
    for j in range(1, n):
            if matrix[0][j] == 1:
                distances[j+1] = 1
            else:
                distances[j+1] = float("inf")
    
    
    while len(visited) != n:
        min_dis = float("inf")
        chosen = None
        for k in distances.keys():
            if k in visited:
                continue
            if (min_dis > distances[k]):
                chosen = k
                min_dis = distances[k]
        visited.append(chosen)
        for j in range(0, n):
            if (matrix[chosen-1][j] == 1):
                if (distances[j+1]) > (min_dis + matrix[chosen-1][j]):
                    distances[j+1] = min_dis + matrix[chosen-1][j]
    print(distances[n])
    
            
