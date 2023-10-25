def divisor(num):
    cnt = 0
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 2
    else:
        for i in range(1, int(num**(1/2))+1):
            if num % i == 0:
                if num == i*i:
                    cnt += 1
                else:
                    cnt += 2
        return cnt
def solution(number, limit, power):
    answer = 0
    number_list = list(range(1, number+1))
    divisor_list = []
    for num in number_list:
        divisor_list.append(divisor(num))
    
    for divisor_num in divisor_list:
        if divisor_num > limit:
            answer += power
        else:
            answer += divisor_num
    return answer