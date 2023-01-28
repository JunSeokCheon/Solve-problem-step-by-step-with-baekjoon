# 시간초과
# import sys
# from collections import defaultdict

# N, M = map(int, sys.stdin.readline().split())
# N_dic = defaultdict(int)
# M_list = []
# for i in range(N):
#     poken = sys.stdin.readline().strip()
#     N_dic[poken] += i+1

# for _ in range(M):
#     M_list.append(sys.stdin.readline().strip())

# for answer in M_list:
#     if answer.isdigit():
#         for key, value in N_dic.items():
#             if int(answer) == value:
#                 print(key)
#     else:
#         for key, value in N_dic.items():
#             if answer == key:
#                 print(value)


# name <-> index 구성된 2개의 딕셔너리 구성
import sys

N, M = map(int, sys.stdin.readline().split())
name_dic = {}
index_dic = {}

for i in range(N):
    poken = sys.stdin.readline().strip()
    name_dic[poken] = i+1
    index_dic[i+1] = poken

for _ in range(M):
    answer = sys.stdin.readline().strip()

    if answer.isdigit():
        print(index_dic[int(answer)])
    else:
        print(name_dic[answer])