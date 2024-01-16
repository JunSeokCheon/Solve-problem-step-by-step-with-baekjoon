def solution(n):
    answer = 1
    
    for i in range(1, n//2+1):
        num_sum = 0
        
        while num_sum < n:
            num_sum += i
            
            if num_sum == n:
                answer += 1
                break
            
            i += 1
            
    return answer