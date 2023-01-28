import sys

N, M = map(int, sys.stdin.readline().split())
N_list = []
M_list = []

for _ in range(N):
    N_list.append(sys.stdin.readline().strip())

for _ in range(M):
    M_list.append(sys.stdin.readline().strip())

result = sorted(set(N_list)&set(M_list))
print(len(result))
for answer in result:
    print(answer)