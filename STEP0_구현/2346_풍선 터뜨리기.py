import sys
from collections import deque

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
que = deque([i for i in range(1, n+1)])
n_dic = {}
result = []

for index, num in enumerate(n_list):
    n_dic[index+1] = num

while que:
    num = que.popleft()
    result.append(num)
    move = n_dic[num]

    if move > 0:
        que.rotate(1-move)
    else:
        que.rotate(-move)

for answer in result:
    print(answer, end=' ')