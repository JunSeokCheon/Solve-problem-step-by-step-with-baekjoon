# 시간 초과
# from itertools import permutations

# def solution(n, k):
#     answer = []
#     n_list = [num for num in range(1, n+1)]
#     n_list_permute = permutations(n_list, n)
#     answer = list(n_list_permute)
#     return answer[k-1]

import math
 
def solution(n, k):
    arr = [i for i in range(1, n + 1)]
    answer = []
    
    while arr:
        a = (k - 1) // math.factorial(n - 1)
        answer.append(arr.pop(a))
        k = k % math.factorial(n - 1)
        n -= 1
    return answer