def merge_sort(LIST):
    if len(LIST) == 1:
        return LIST
    
    q = (len(LIST)+1) // 2
    
    L = merge_sort(LIST[:q]);  # 전반부 정렬
    R = merge_sort(LIST[q:]);  # 후반부 정렬
    
    i = 0
    j = 0
    tmp = []
    
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            tmp.append(L[i])
            answer.append(L[i])
            i += 1
        else:
            tmp.append(R[j])
            answer.append(R[j])
            j += 1
    
    while i < len(L):
        tmp.append(L[i])
        answer.append(L[i])
        i += 1
    
    while j < len(R):
        tmp.append(R[j])
        answer.append(R[j])
        j += 1
        
    return tmp
    
import sys
input = sys.stdin.readline
 
N, K = map(int, input().split())
LIST = list(map(int, input().split()))
 
answer = []
merge_sort(LIST)
if len(answer) < K:
    print(-1)
else:
    print(answer[K-1])