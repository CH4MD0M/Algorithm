num_dict = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

def solution(strings):
    answer = ''
    tmp = ''
    for s in strings:
        if s.isdigit():
            answer += str(s)
        else:
            tmp += str(s)
            
        if tmp in num_dict.keys():
            answer += str(num_dict[tmp])
            tmp = ''
            
    return int(answer)

# 다른 풀이
table = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def solution(s):
    answer = s
    for key, value in table.items():
        answer = answer.replace(key, value)
    return int(answer)

