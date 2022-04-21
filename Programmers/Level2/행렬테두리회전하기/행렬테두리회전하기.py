def solution(rows, columns, queries):
    answer = []
    matrix = [[0 for _ in range(columns+1)] for _ in range(rows+1)]
    v = 1
    for r in range(1, rows+1):
        for c in range(1, columns+1):
            matrix[r][c] = v
            v += 1
            
    for x1, y1, x2, y2 in queries:
        check = matrix[x1][y1]
        _min = check    
        
        # 왼쪽 세로
        for i in range(x1, x2):
            tmp = matrix[i+1][y1]
            matrix[i][y1] = tmp
            _min = min(_min, tmp)
            
        # 하단 가로
        for i in range(y1, y2):
            tmp = matrix[x2][i+1]
            matrix[x2][i] = tmp
            _min = min(_min, tmp)            

        # 오른쪽 세로
        for i in range(x2, x1, -1):
            tmp = matrix[i-1][y2]
            matrix[i][y2] = tmp
            _min = min(_min, tmp)

        # 상단 가로
        for i in range(y2, y1, -1):
            tmp = matrix[x1][i-1]
            matrix[x1][i] = tmp
            _min = min(_min, tmp)        
            
        matrix[x1][y1+1] = check
        answer.append(_min)

    return answer