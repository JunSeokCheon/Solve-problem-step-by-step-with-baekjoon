def solution(n, m, section):
    answer = 1
    
    init = section[0]
    
    for sect in section:
        # 롤러로 칠할 수 없는 구역이면
        if init + (m-1) < sect:
            init = sect
            answer += 1
    
    return answer