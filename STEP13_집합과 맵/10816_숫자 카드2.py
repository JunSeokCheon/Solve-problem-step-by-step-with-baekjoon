import sys

M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))
N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
M_dic = {}

for num in M_list:
    if num not in M_dic:
        M_dic[num] = 1
    else:
        M_dic[num] += 1

for num in N_list:
    if M_dic.get(num):
        print(M_dic[num], end=' ')
    else:
        print(0, end=' ')