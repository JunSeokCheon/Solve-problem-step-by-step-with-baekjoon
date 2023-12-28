def solution(elements):
    answer_list = []
    ele_len = len(elements)
    elements *= 2
    
    for i in range(ele_len):
        for j in range(1, ele_len+1):
            answer_list.append(sum(elements[i:i+j]))    
    
    return len(set(answer_list))