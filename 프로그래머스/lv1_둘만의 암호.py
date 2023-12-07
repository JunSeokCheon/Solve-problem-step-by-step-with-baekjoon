def solution(s, skip, index):
    answer = ''
    
    for mini_s in s:
        mini_s_asc = ord(mini_s)
        index_i = index
        
        while index_i > 0:
            mini_s_asc += 1
            if mini_s_asc > ord('z'):
                mini_s_asc = ord('a')
            if chr(mini_s_asc) in skip:
                index_i += 1
            index_i -= 1
        answer += chr(mini_s_asc)
        
    return answer