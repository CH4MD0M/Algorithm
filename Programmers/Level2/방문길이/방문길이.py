def solution(dirs):
    direction = {'U': 0, 'D': 1, 'R': 2, 'L':3}
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited = set()
    x, y = 0, 0
    
    for d in dirs:
        i = direction[d]
        nx = x + dx[i]
        ny = y + dy[i]
    
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            visited.add((x, y, nx, ny))
            visited.add((nx, ny, x, y))
            x, y = nx, ny
    
    return len(visited) // 2