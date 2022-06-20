def solution(numbers, hand):
    answer = ''
    keyPad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2), 
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2) 
    }
    left = [1, 4, 7]
    right = [3, 6, 9]
    l_hand = '*'
    r_hand = '#'
    
    for i in numbers:
        if i in left:
            answer += 'L'
            l_hand = i
        elif i in right:
            answer += 'R'
            r_hand = i
        else:
            cur = keyPad[i]
            l_position = keyPad[l_hand]
            r_position = keyPad[r_hand]
            l_dist = abs(cur[0] - l_position[0]) + abs(cur[1] - l_position[1])
            r_dist = abs(cur[0] - r_position[0]) + abs(cur[1] - r_position[1])
            
            if l_dist > r_dist:
                r_hand = i
                answer += 'R'
            elif l_dist < r_dist:
                l_hand = i
                answer += 'L'
            else:
                if hand =='right':
                    r_hand = i
                    answer += 'R'
                else:
                    l_hand = i
                    answer += 'L'
                    
    return answer