# 시간초과
# import sys

# N = int(sys.stdin.readline())
# n_list = list(map(int, sys.stdin.readline().split()))
# M = int(sys.stdin.readline())
# M_list = list(map(int, sys.stdin.readline().split()))


# n_list = list(set(n_list))
# for i in M_list:
#     if i in n_list:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')


# 딕셔너리 사용
import sys

N = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))
n_dic = {}
m_dic = {}

n_list = list(set(n_list))

for i in n_list:
    if i not in n_dic:
        n_dic[i] = 1
    else:
        n_dic[i] += 1

for i in M_list:
    if i not in m_dic:
        m_dic[i] = 1
    else:
        m_dic[i] += 1

for key in m_dic.keys():
    if n_dic.get(key):
        print(1, end=' ')
    else:
        print(0, end=' ')