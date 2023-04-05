# [2, 1, 1, 0] -> 4 2 1 3
import sys

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
answer = [0] * n

for i in range(n):
    zero_cnt = 0

    for j in range(n):
        if zero_cnt == n_list[i] and answer[j] == 0:
            answer[j] = i + 1
            break
        elif answer[j] == 0:
            zero_cnt += 1

print(*answer)