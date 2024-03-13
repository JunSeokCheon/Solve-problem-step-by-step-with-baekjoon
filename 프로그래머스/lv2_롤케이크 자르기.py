from collections import Counter

def solution(topping):
    answer = 0
    chul = Counter(topping)
    brother_dic = {}
    
    for top in topping:
        if top not in brother_dic:
            brother_dic[top] = 1
        else:
            brother_dic[top] += 1
        
        chul[top] -= 1
        
        if chul[top] == 0:
            del chul[top]
        
        if len(brother_dic) == len(chul):
            answer += 1
        
    return answer