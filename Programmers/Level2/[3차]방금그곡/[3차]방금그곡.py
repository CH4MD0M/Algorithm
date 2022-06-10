def solution(m, musicinfos):
    answer = []
    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
    
    for musicinfo in musicinfos:
        start, end, title, code = musicinfo.split(',')
        
        start_hour, start_minute = map(int, start.split(':'))
        end_hour, end_minute = map(int, end.split(':'))
        duration = (end_hour - start_hour) * 60 + end_minute - start_minute
        
        code = code.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
        code *= (duration // len(code)) + 1
        code = code[:duration]
        
        if m in code:
            answer.append([duration, start_hour * 60 + start_minute, title])
    
    if answer:
        return sorted(answer, key=lambda x:(-x[0], x[1]))[0][-1]
    return "(None)"