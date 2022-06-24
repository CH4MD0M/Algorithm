def solution(m, n, board):
    answer = 0
    board = [list(i) for i in board]
    
    while True:
        check = [[0 for c in range(n)] for r in range(m)]
        # 블럭 찾기
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] != 0 and board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    check[i][j], check[i][j+1], check[i+1][j], check[i+1][j+1] = 1, 1, 1, 1
        
        # 제거한 블럭 count
        count = 0
        for i in range(m):
            count += sum(check[i])
        if count == 0:
            break
        answer += count
        
        # 블럭 이동
        for i in range(m-1, -1, -1):
            for j in range(n):
                if check[i][j] == 1:
                    x = i-1
                    while x >= 0 and check[x][j] == 1:
                        x -= 1
                    if x < 0:
                        board[i][j] = 0
                    else:
                        board[i][j] = board[x][j]
                        check[x][j] = 1
    return answer
    