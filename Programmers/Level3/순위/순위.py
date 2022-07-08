def solution(n, results):
    INF = int(1e9)
    matrix = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
    
    for win, lose in results:
        matrix[win][lose] = True
        matrix[lose][win] = False
    
    for k in range(n + 1):
        for i in range(n + 1):
            for j in range(n + 1):
                if matrix[i][k] == INF:
                    continue
                    
                if matrix[i][k] == matrix[k][j]:
                    matrix[i][j] = matrix[i][k]
                    matrix[j][i] = not matrix[i][k]
    
    return len([m for m in matrix if m.count(INF) == 2])