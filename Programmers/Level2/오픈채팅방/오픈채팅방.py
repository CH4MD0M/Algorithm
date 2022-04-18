def solution(record):
    answer = []
    _dict = {}
    for r in record:
        _split = r.split()
        if len(_split) == 3:
            _dict[_split[1]] = _split[2]
    
    for r in record:
        _split = r.split()
        if _split[0] == "Enter":
            answer.append("{}님이 들어왔습니다.".format(_dict[_split[1]]))
        elif _split[0] == "Leave":
            answer.append("{}님이 나갔습니다.".format(_dict[_split[1]]))
    return answer