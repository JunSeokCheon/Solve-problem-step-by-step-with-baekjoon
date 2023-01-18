# 시간초과 - num의 제곱근까지 비교 - pyp3로는 성공
# import sys

# def solve(num):
#     count = 0
#     if num < 2:
#         return 1
#     else:
#         for mini_num in range(num+1, num*2+1):
#             flag = True
#             for i in range(2, int(mini_num**0.5)+1):
#                 if mini_num % i == 0:
#                     flag = False
#                     break
            
#             if flag == True:
#                 count += 1
#             else:
#                 pass
#         return count

# while(True):
#     num = int(sys.stdin.readline())
#     if num == 0:
#         break
#     result = solve(num)
#     print(result)

# 에라토스테네스의 체
import sys

eratos = [0] * 2 + [1] * 246912

for i in range(2, 246913):
    if eratos[i]:
        for j in range(i * 2, 246913, i):
            eratos[j] = 0

while(True):
    num = int(sys.stdin.readline())
    if num == 0:
        break
    print(sum(eratos[num+1:num*2+1]))