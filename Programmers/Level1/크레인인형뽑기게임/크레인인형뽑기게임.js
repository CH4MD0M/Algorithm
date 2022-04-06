function solution(board, moves) {
    let result = [],
        answer = 0;

    for (let m = 0; m < moves.length; m++) {
        for (let i = 0; i < board.length; i++) {
            if (board[i][moves[m] - 1] !== 0) {
                result.push(board[i][moves[m] - 1]);
                board[i][moves[m] - 1] = 0;

                if (
                    result.length != 1 &&
                    result[result.length - 1] === result[result.length - 2]
                ) {
                    answer += 2;
                    result = result.slice(0, -2);
                }
                break;
            }
        }
    }

    return answer;
}
