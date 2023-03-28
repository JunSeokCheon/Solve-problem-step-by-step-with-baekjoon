import sys
import heapq

n = int(sys.stdin.readline())

max_heap = []
min_heap = []

for _ in range(n):
    num = int(sys.stdin.readline())

    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)
    
    if max_heap and min_heap and -max_heap[0] > min_heap[0]:
        max_num = heapq.heappop(max_heap)
        heapq.heappush(min_heap, -max_num)

        min_num = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -min_num)
    
    print(-max_heap[0])
        