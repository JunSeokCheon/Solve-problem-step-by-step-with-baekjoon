import sys

N, k = map(int, sys.stdin.readline().split())
n_list = list(map(int, sys.stdin.readline().split()))

n_list.sort(reverse=True)
print(n_list[k-1])