from itertools import combinations
import sys

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
m = sum(n_list)
combi_num = set()

for i in range(1, n+1):
    for j in combinations(n_list, i):
        combi_num.add(sum(j))

print(m-len(combi_num))
