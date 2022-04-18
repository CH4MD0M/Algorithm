function solution(record) {
    let answer = [];
    _map = new Map();

    for (let r of record) {
        _split = r.split(" ");

        _split.length === 3 && _map.set(_split[1], _split[2]);
    }

    for (let r of record) {
        _split = r.split(" ");
        if (_split[0] == "Enter") {
            answer.push(`${_map.get(_split[1])}님이 들어왔습니다.`);
        } else if (_split[0] == "Leave") {
            answer.push(`${_map.get(_split[1])}님이 나갔습니다.`);
        }
    }

    return answer;
}
