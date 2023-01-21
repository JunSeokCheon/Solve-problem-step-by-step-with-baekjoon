import sys

N = int(sys.stdin.readline())
n_list = []

for _ in range(N):
    age, name = map(str, sys.stdin.readline().strip().split())
    n_list.append((int(age),name))

result = sorted(n_list, key = lambda x : (x[0]))
for answer in result:
    print(answer[0], answer[1], sep=' ')