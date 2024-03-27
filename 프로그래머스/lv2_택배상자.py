def solution(order):
    answer = 0
    # stack = 보조 컨테이너 벨트
    stack = []
    order_idx = 0
    
    for i in range(1, len(order)+1):
        stack.append(i)
        while stack and stack[-1] == order[order_idx]:
            stack.pop()
            order_idx += 1
            answer += 1
            
    return answer