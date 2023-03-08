import sys
from collections import deque

A, B = map(int, sys.stdin.readline().split())
que = deque()
que.append((A, 1))

while que:
    num, cnt = que.popleft()

    if num > B:
        continue
    if num == B:
        print(cnt)
        break

    que.append((int(str(num)+"1"), cnt+1))
    que.append((num*2, cnt+1))
else:
    print(-1)