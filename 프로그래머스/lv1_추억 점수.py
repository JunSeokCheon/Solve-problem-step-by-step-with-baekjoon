from collections import defaultdict

def solution(name, yearning, photo):
    answer = []
    name_year_dic = defaultdict(int)
    for mini_name, mini_year in zip(name,yearning):
        name_year_dic[mini_name] = mini_year

    for mini_photo in photo:
        result = 0
        for names in mini_photo:
            result += name_year_dic[names]
        answer.append(result)
    
    return answer