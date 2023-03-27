import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x > 0:
        heapq.heappush(heap, -x)
    elif x == 0 and len(heap) == 0:
        print(0)
    else:
        num = heapq.heappop(heap)
        print(-num)

