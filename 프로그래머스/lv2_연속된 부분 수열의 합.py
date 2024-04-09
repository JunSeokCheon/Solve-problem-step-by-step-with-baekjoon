# 연속합 = k
# 1. 최소 원소
# 2. 최저 인덱스

# 실패 : 실행한 결괏값 [2,4]이 기댓값 [0,2]과 다릅니다.
# 연속합이 k가 같은 때, 최소 인덱스를 만족하지 못함.
# def solution(sequence, k):
#     num = 0
    
#     for i in range(len(sequence)-1, -1, -1):
#         num += sequence[i]
#         if num > k:
#             num -= sequence.pop()
        
#         if num == k:
#             return [i, len(sequence)-1]

def solution(sequence, k):
    num = 0
    
    for i in range(len(sequence)-1, -1, -1):
        num += sequence[i]
        if num > k:
            num -= sequence.pop()
        
        if num == k:
            while sequence[i-1] == sequence[-1] and i > 0:
                i -= 1
                sequence.pop()
            return [i, len(sequence)-1]