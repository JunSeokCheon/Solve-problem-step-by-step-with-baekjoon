def solution(s):
    answer = 0
    max_len = len(s)
    
    stand_num = s[0]
    stand_cnt = 1
    diff_cnt = 0
    idx = 0
    
    while True:
        if len(s) == 1:
            answer += 1
            break 
        idx += 1
        if s[idx] == stand_num:
            stand_cnt += 1
        else:
            diff_cnt += 1
        
        if stand_cnt == diff_cnt and len(s) == idx+1:
            answer += 1
            break
        elif stand_cnt == diff_cnt:
            answer += 1
            s = s[idx+1:]
            stand_num = s[0]
            stand_cnt = 1
            diff_cnt = 0
            idx = 0
        elif len(s) == idx + 1:
            answer += 1
            break
     
    return answer

# print(solution("banana"))
# print(solution("ab"))

