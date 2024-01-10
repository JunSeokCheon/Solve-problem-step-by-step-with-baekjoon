import math

def solution(n):
    temp = int(math.sqrt(n))
    if temp * temp == n:
        return int((temp+1) ** 2)
    else:
        return -1

print(solution(121))
print(solution(3))
print(solution(1))
print(solution(2))
print(solution(101))
print(solution(4))