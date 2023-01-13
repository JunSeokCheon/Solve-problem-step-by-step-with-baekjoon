import sys

N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
V = int(sys.stdin.readline())

print(N_list.count(V))