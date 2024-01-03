def solution(t, p):
    answer = 0
    len_p = len(p)
    
    for i in range(len(t)):
        part_num = t[i:i+len_p]
        
        if len(part_num) == len_p:
            if int(p) >= int(part_num):
                answer += 1
    return answer