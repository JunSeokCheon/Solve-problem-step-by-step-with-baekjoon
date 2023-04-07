import heapq

def solution(k, score):
    answer = []
    heap = []
    
    for mini_score in score:
        if len(heap) >= k:
            heapq.heappush(heap, mini_score)
            heapq.heappop(heap)
            result = heapq.heappop(heap)
            answer.append(result)
            heapq.heappush(heap, result)
        else:
            heapq.heappush(heap, mini_score)
            result = heapq.heappop(heap)
            answer.append(result)
            heapq.heappush(heap, result)
    
    return answer