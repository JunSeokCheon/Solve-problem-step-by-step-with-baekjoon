import sys

n, m = map(int, sys.stdin.readline().split())
n_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
m, k = map(int, sys.stdin.readline().split())
m_list = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

result = [[0]*k for _ in range(n)]
for i in range(n):
    for j in range(m):
        for z in range(k):
            result[i][z] += n_list[i][j] * m_list[j][z]

for answer in result:
    print(*answer)