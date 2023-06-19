# pypy3 제출 - dp로 풀면 python3로 통과할수도?
import sys

n, m = map(int, sys.stdin.readline().split())
num_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
k = int(sys.stdin.readline())
orders = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]
result = []

for order in orders:
    num_sum = 0
    i, j, x, y = order
    
    for a in range(i-1, x):
        for b in range(j-1, y):
            num_sum += num_list[a][b]
    result.append(num_sum)

for answer in result:
    print(answer)