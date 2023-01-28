import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().split())
N_dic = defaultdict(int)
M_list = []
count = 0

for _ in range(N):
    S = sys.stdin.readline().strip()
    N_dic[S] += 1

for _ in range(M):
    C = sys.stdin.readline().strip()
    M_list.append(C)

for key in M_list:
    if N_dic.get(key):
        count += 1

print(count)