import sys

N = int(sys.stdin.readline())
n_list = []

for _ in range(N):
    n_list.append(sys.stdin.readline().strip())

n_list = set(n_list)
result = sorted(n_list, key = lambda x : (len(x),x))

for char in result:
    print(char)
