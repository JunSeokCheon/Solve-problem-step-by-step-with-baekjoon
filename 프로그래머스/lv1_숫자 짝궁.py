def solution(X, Y):
    # 가장 큰 정수 
    num_str = "9876543210"
    result = []
    for num in num_str:
        num_count = min(X.count(num), Y.count(num))
        result.append(num*num_count)
    
    answer = ''.join(result)
    if answer:
        if answer[0] == '0':
            answer = '0'
    else:
        answer = '-1'        
    
    return answer