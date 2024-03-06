# # 시간 초과
# def solution(n, left, right):
#     answer = []
#     two_diem_matrix = [[0] * n for _ in range(n)]
    
#     for i in range(1, n+1):
#         for j in range(i):
#             for k in range(i):
#                 if two_diem_matrix[j][k] == 0:
#                     two_diem_matrix[j][k] = i
                    
#     new_matrix = sum(two_diem_matrix, [])
#     for i in range(left, right+1):
#         answer.append(new_matrix[i])
#     return answer


# 먼저 제한사항을 보면 n이 10^7일 때, 배열을 모두 채워가며 슬라이싱은 불가하다라는 것을 판단해야 한다. -> 제한사항 필독
# 대각선 값을 기준으로 왼쪽 직선과 위쪽 직선은 같은 값을 가지고 있다는 것을 발견하고, 번째(i)와 n을 조합하면 해결책이 나온다는 것을 인지한다.
# i//n, i%n 중 큰 값에 + 1
def solution(n, left, right):
    answer = []
    
    for i in range(left, right+1):
        x,y = i//n, i%n
        answer.append(max(x,y)+1)
    
    return answer