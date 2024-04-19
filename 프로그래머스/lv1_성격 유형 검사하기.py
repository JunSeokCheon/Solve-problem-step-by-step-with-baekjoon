from collections import defaultdict

def solution(survey, choices):
    answer = ''
    
    type_table = ["RT", "CF", "JM", "AN"]
    score_dic = {1:3, 2:2, 3:1, 5:1, 6:2, 7:3}
    total_dic = defaultdict(int)
    
    for i in range(len(survey)):
        disagree, agree = survey[i][0], survey[i][1]
        
        if choices[i] in [1,2,3]:
            total_dic[disagree] += score_dic[choices[i]]
        
        if choices[i] in [5,6,7]:
            total_dic[agree] += score_dic[choices[i]]

    for word_type in type_table:
        if total_dic[word_type[0]] >= total_dic[word_type[1]]:
            answer += word_type[0]
        else:
            answer += word_type[1]
    
    return answer