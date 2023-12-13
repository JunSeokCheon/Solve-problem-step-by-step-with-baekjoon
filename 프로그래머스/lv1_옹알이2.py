def solution(babbling):
    answer = 0
    orders = ["aya", "ye", "woo", "ma"]
    
    for babb in babbling:
        for order in orders:
            if (order in babb) and (order*2 not in babb):
                babb = babb.replace(order, " ")
        babb = babb.replace(" ", "")
        if len(babb) == 0:
            answer += 1
    return answer