import sys

A, B = map(int, sys.stdin.readline().split())
A_list = list(map(int, sys.stdin.readline().split()))
B_list = list(map(int, sys.stdin.readline().split()))

print(len((set(A_list)^set(B_list))))