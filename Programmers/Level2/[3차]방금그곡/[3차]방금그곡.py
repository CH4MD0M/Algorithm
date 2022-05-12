import math

def solution(m, musicinfos):
    answer = []
    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
    
    for musicinfo in musicinfos:
        start, end, title, code = musicinfo.split(',')
        
        start_h, start_m = map(int, start.split(':'))
        end_h, end_m = map(int, end.split(':'))
        duration = (end_h - start_h) * 60 + end_m - start_m
        
        code = code.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
        code *= math.ceil(duration / len(code))
        code = code[:duration]
        
        if m in code:
            answer.append([duration, start_h * 60 + start_m, title])
    
    if answer:
        answer = sorted(answer, key=lambda x:(-x[0], x[1]))[0][-1]
        return answer
    return "(None)"
