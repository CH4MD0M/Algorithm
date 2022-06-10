def solution(cacheSize, cities):
    cache = []
    time = 0
    
    for city in cities:
        city = city.lower()
        if cacheSize:
            if city not in cache:
                cache.append(city)
                if len(cache) > cacheSize:
                    cache.pop(0)
                time += 5
            else:
                cache.remove(city)
                cache.append(city)
                time += 1
        else:
            time += 5
    return time

'''
LRU 페이지 교체 알고리즘 사용.
Cache Hit: CPU가 참조하고자 하는 메모리가 캐시에 존재하고 있을 경우
Cache Miss: CPU가 참조하고자 하는 메모리가 캐시에 존재하지 않을 경우

CachSize가 0인 케이스 가 있기 때문에 따로 조건문을 사용하는 것이 나은 코드라고 생각한다.
조건문을 사용하지 않아도 오류는 발생하지 않음.
'''