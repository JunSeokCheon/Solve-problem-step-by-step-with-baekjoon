def solution(dirs):
    answer = 0
    board = []
    # 초기 위치는 (5,5)
    init_x = 5
    init_y = 5
    directions = {'U':(0, -1), 'D':(0, 1), 'R':(1, 0), 'L':(-1, 0)}
    
    for i in range(len(dirs)):
        # 위치에 따른 좌표 저장
        dx, dy = directions[dirs[i]]
        # board 판을 넘으면 무시
        if init_x + dx < 0 or init_x + dx > 10 or init_y + dy < 0 or init_y + dy > 10:
            continue
        # 역방향을 계산하기 위해서 역방향 좌표도 같이 넣어주자
        board.append((init_x, init_y, init_x+dx, init_y+dy))
        board.append((init_x+dx, init_y+dy, init_x, init_y))
        init_x = init_x + dx
        init_y = init_y + dy
    
    # set을 활용한 중복 좌표 제거
    board = set(board)
    # 길이 계산
    answer = len(board)//2
    return answer