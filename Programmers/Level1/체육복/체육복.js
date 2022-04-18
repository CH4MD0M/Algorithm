function solution(n, lost, reserve) {
    let _lost = lost.filter((v) => !reserve.includes(v));
    let _reserve = reserve.filter((v) => !lost.includes(v));

    for (let i = 0; i < _reserve.length; i++) {
        if (_lost.includes(_reserve[i] - 1)) {
            _lost = _lost.filter((v) => v !== _reserve[i] - 1);
        } else if (reserve.includes(lost[i] + 1)) {
            _lost = _lost.filter((v) => v !== _reserve[i] + 1);
        }
    }
    return n - _lost.length;
}
