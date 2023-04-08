def solution(cards1, cards2, goal):
    answer = 'Yes'
    card1_index = 0
    card2_index = 0
    
    for word in goal:
        if word in cards1 and cards1.index(word) == card1_index:
            card1_index += 1
        elif word in cards2 and cards2.index(word) == card2_index:
            card2_index += 1
        else:
            answer = 'No'
            break
        
    return answer