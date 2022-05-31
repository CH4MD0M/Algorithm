def solution(genres, plays):
    answer = []
    genre_dict = {}
    
    play_lst = [(genres[i], plays[i], i) for i in range(len(genres))] 
    play_lst = sorted(play_lst, key=lambda x:(x[0], -x[1], x[2]))
    
    for genre in play_lst:
        if genre[0] in genre_dict:
            genre_dict[genre[0]] += genre[1]
        else:
            genre_dict[genre[0]] = genre[1]
            
    genre_dict = sorted(genre_dict.items(), key=lambda x: -x[1])
    
    for i in genre_dict:
        count = 0
        for j in play_lst:
            if i[0] == j[0]:
                count += 1
                if count > 2:
                    break
                else:
                    answer.append(j[2])
    
    return answer