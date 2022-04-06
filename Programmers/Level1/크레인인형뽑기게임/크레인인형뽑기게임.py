def solution(board, moves):
    result = []
    answer = 0
    for m in moves:
        for i in range(len(board)):
            if board[i][m - 1] != 0:
                result.append(board[i][m - 1])
                board[i][m - 1] = 0
                
                if len(result) > 1:
                    if result[-1] == result[-2]:
                        answer += 2
                        result = result[:-2]
                break
    return answer