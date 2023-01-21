import sys

N = int(sys.stdin.readline())
n_list = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    n_list.append((x,y))

result = sorted(n_list, key = lambda x : (x[1], x[0]))
for answer in result:
    print(answer[0], answer[1], sep=' ')