# 계수(카운팅) 정렬 - 이론대로 그대로 했지만 메모리 초과
# import sys

# N = int(sys.stdin.readline())
# n_list = []
# count = [0] * (10001)

# for _ in range(N):
#     n_list.append(int(sys.stdin.readline()))

# for num in n_list:
#     count[num] += 1

# for i in range(1, len(count)):
#     count[i] += count[i-1]

# result = [0] * N

# for num in n_list:
#     idx = count[num]
#     result[idx-1] = num
#     count[num] -= 1

# for num in result:
#     print(num)


# 계수(카운팅) 정렬 계량 버전
import sys

N = int(sys.stdin.readline())
n_list = [0] * 10001

for i in range(N):
    num = int(sys.stdin.readline())
    n_list[num] = n_list[num] + 1

for i in range(1, 10001):
    if n_list[i] != 0:
        for j in range(n_list[i]):
            print(i)
