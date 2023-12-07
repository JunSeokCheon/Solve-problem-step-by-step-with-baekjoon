import sys
from collections import deque

n = int(sys.stdin.readline())
que = deque([i for i in range(1, n+1)])
result = []

while len(que) != 0:
    result_num = que.popleft()
    result.append(result_num)
    if len(que) == 0:
        break
    num = que.popleft()
    que.append(num)
print(*result)