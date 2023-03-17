import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    N_list = list(map(str, sys.stdin.readline().strip().split()))
    que = deque()
    que.append(N_list[0])
    stanard = N_list[0]

    for i in range(1, N):
        if stanard >= N_list[i]:
            que.appendleft(N_list[i])
            stanard = N_list[i]
        else:
            que.append(N_list[i])
    print(''.join(que))