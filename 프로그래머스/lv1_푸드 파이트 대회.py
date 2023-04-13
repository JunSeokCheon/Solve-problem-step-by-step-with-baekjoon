def solution(food):
    answer = ''
    
    for index, value in enumerate(food[1:]):
        count = value//2
        if count == 0:
            continue
        answer += str(index+1) * count
    
    answer = answer + "0" + answer[::-1]
    return answer