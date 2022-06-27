def solution(s):
    zero_count, bin_count = 0, 0

    while len(s)>1:            
        zero_count += s.count('0')
        s = format(len(s.replace('0','')), 'b')
        bin_count += 1
        
    return [bin_count, zero_count]
