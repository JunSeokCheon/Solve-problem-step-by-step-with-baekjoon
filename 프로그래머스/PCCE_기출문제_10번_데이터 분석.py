def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    temp = []
    data_condition = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    
    ext = data_condition[ext]
    sort_by = data_condition[sort_by]
    
    for mini_data in data:
        if mini_data[ext] < val_ext:
            temp.append(mini_data)
    
    answer = sorted(temp, key = lambda x : x[sort_by])
    
    return answer