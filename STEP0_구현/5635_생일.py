import sys

n = int(sys.stdin.readline())
n_list = []

for _ in range(n):
    name, day, month, year = map(str, sys.stdin.readline().split())
    n_list.append((name, int(day), int(month), int(year)))

n_list.sort(key = lambda x : (x[3], x[2], x[1]))
print(n_list[-1][0])
print(n_list[0][0])