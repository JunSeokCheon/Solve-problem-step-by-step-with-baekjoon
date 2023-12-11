from itertools import combinations

def solution(number):
    answer = 0
    
    for combin in list(combinations(number, 3)):
        if sum(combin) == 0:
            answer += 1
    
    return answer