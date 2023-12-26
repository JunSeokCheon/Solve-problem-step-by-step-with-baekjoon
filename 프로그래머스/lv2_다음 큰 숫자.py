def solution(n): 
    temp_n = n
    result = bin(n)[2:]
    cnt = result.count("1")

    while True:
        temp_n += 1                                
        compare_num = bin(temp_n)[2:]
        compare_cnt = compare_num.count("1")

        if cnt == compare_cnt:
            break

    return temp_n