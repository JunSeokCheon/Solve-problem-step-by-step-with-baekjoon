def solution(bandage, health, attacks):
    answer = 0
    last_attack_time = attacks[-1][0]
    origin_health = health
    continue_attack_count = 0
    
    attack_dic = {}
    for attack in attacks:
        attack_dic[attack[0]] = attack[1]
    
    for i in range(1, last_attack_time+1):   
        if i in attack_dic:
            health -= attack_dic[i]
            continue_attack_count = 0
        else:
            if origin_health <= health:
                health = origin_health
            else:
                health += bandage[1]
                continue_attack_count += 1
                
                if continue_attack_count == bandage[0]:
                    health += bandage[2]
                    continue_attack_count = 0
        if health <= 0:
            return -1

    return health   