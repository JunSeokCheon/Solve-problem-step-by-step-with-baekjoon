import sys

N, X = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
new_list = []

for num in A:
    if X > num:
        new_list.append(str(num))

print(' '.join(new_list))