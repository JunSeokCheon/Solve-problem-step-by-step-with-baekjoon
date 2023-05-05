from collections import defaultdict

def solution(players, callings):
    dic = defaultdict(int)
    
    for index, player in enumerate(players):
        dic[player] = index
        
    for call in callings:
        order = dic[call]
        dic[call] -= 1
        dic[players[order-1]] += 1
        players[order-1], players[order] = players[order], players[order-1]
    
    return players