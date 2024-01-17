from collections import Counter

def solution(k, tangerine):
    answer = 0
    tangerine = Counter(tangerine)
    sorted_tangerine = sorted(tangerine.items(), key = lambda x : x[1], reverse = True)
    
    for keys, values in sorted_tangerine:
        if k <= 0:
            break
        k -= values
        answer += 1
    return answer