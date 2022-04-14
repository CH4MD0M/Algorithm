table = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
}

def solution(string):
    answer = ''
    alp = ''
    for c in string:
        if c.isdigit():
            answer += str(c)
        else:
            alp += c
        
        if alp in table.keys():
            answer += str(table[alp])
            alp = ''
            
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

