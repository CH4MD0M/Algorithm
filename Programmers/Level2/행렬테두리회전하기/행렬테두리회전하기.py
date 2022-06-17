def solution(rows, columns, queries):
    answer = []
    matrix = [[0 for _ in range(columns + 1)]for _ in range(rows + 1)]
    
    value = 1
    for r in range(1, rows + 1):
        for c in range(1, columns + 1):
            matrix[r][c] = value
            value += 1
            
    for x1, y1, x2, y2 in queries:
        tmp_value = matrix[x1][y1]
        min_value = tmp_value
        
        for i in range(x1, x2):
            tmp = matrix[i + 1][y1]
            matrix[i][y1] = tmp
            min_value = min(min_value, tmp)
        
        for i in range(y1, y2):
            tmp = matrix[x2][i + 1]
            matrix[x2][i] = tmp
            min_value = min(min_value, tmp)
            
        for i in range(x2, x1, -1):
            tmp = matrix[i - 1][y2]
            matrix[i][y2] = tmp
            min_value = min(min_value, tmp)
            
        for i in range(y2, y1, -1):
            tmp = matrix[x1][i - 1]
            matrix[x1][i] = tmp
            min_value = min(min_value, tmp)
        
        matrix[x1][y1 + 1] = tmp_value
        answer.append(min_value)
        
    return answer