import sys
from itertools import permutations

n = int(sys.stdin.readline())
num_list = list(permutations([1,2,3,4,5,6,7,8,9], 3))

for _ in range(n):
    number, strike, ball = map(int, sys.stdin.readline().split())
    number = list(str(number))
    remove_cnt = 0
    
    for i in range(len(num_list)):
        strike_cnt, ball_cnt = 0, 0
        i -= remove_cnt

        for j in range(3):
            number[j] = int(number[j])
            if number[j] in num_list[i]:
                if j == num_list[i].index(number[j]):
                    strike_cnt += 1
                else:
                    ball_cnt += 1
        
        if strike_cnt != strike or ball_cnt != ball:
            num_list.remove(num_list[i])
            remove_cnt += 1

print(len(num_list))