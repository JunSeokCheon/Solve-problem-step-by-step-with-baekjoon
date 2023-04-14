from collections import defaultdict

def solution(s):
    answer = []
    dic = defaultdict(list)
    
    for index, word in enumerate(s):
        if dic.get(word) == None:
            answer.append(-1)
            dic[word].append(index)
        else:
            answer.append(index-dic[word][-1])
            dic[word].append(index)
        
    return answer