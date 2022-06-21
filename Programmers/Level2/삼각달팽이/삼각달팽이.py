def solution(n):
    matrix = [[0] * n for _ in range(n)]
    x, y = -1, 0
    num = 1
    
    for i in range(n):
        for _ in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            
            matrix[x][y] = num
            num += 1
            
    return [value for inner_matrix in matrix for value in inner_matrix if value != 0]