from collections import Counter

def solution(want, number, discount):
    answer = 0
    wanted_dic = {w:n for w,n in zip(want,number)}
    
    for i in range(len(discount)):
        if wanted_dic == Counter(discount[i:i+10]):
            answer += 1
    
    return answer