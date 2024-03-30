def solution(board):
    answer = 0
    bomb_list = []
    
    new_board = board
    
    for i in range(len(new_board)):
        for j in range(len(new_board[0])):
            if new_board[i][j] == 1:
                bomb_list.append([i,j])

    for x,y in bomb_list:
        left_up = [x-1, y-1]
        left = [x-1, y]
        left_down = [x-1, y+1] 
        up = [x, y-1]
        down = [x, y+1]
        right_up = [x+1, y-1]
        right = [x+1, y]
        right_down = [x+1, y+1]
        
        if left_up[0] < 0 or left_up[0] >= len(new_board[0]) or left_up[1] < 0 or left_up[1] >= len(new_board[0]):
            pass
        else:
            new_board[left_up[0]][left_up[1]] = 1
            
        if left[0] < 0 or left[0] >= len(new_board[0]) or left[1] < 0 or left[1] >= len(new_board[0]):
            pass
        else:
            new_board[left[0]][left[1]] = 1
            
        if left_down[0] < 0 or left_down[0] >= len(new_board[0]) or left_down[1] < 0 or left_down[1] >= len(new_board[0]):
            pass
        else:
            new_board[left_down[0]][left_down[1]] = 1
            
        if up[0] < 0 or up[0] >= len(new_board[0]) or up[1] < 0 or up[1] >= len(new_board[0]):
            pass
        else:
            new_board[up[0]][up[1]] = 1
            
        if down[0] < 0 or down[0] >= len(new_board[0]) or down[1] < 0 or down[1] >= len(new_board[0]):
            pass
        else:
            new_board[down[0]][down[1]] = 1
            
        if right_up[0] < 0 or right_up[0] >= len(new_board[0]) or right_up[1] < 0 or right_up[1] >= len(new_board[0]):
            pass
        else:
            new_board[right_up[0]][right_up[1]] = 1
        
        if right[0] < 0 or right[0] >= len(new_board[0]) or right[1] < 0 or right[1] >= len(new_board[0]):
            pass
        else:
            new_board[right[0]][right[1]] = 1
        
        if right_down[0] < 0 or right_down[0] >= len(new_board[0]) or right_down[1] < 0 or right_down[1] >= len(new_board[0]):
            pass
        else:
            new_board[right_down[0]][right_down[1]] = 1
    for line in new_board:
        answer += line.count(0)
    
    return answer