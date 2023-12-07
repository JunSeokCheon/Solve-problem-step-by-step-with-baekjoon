dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

def solution(board, h, w):
    answer = 0
    n = len(board)
    m = len(board[0])
    target = board[h][w]
    
    for i in range(4):
        nx = h + dx[i]
        ny = w + dy[i]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        
        if target == board[nx][ny]:
            answer += 1

    return answer