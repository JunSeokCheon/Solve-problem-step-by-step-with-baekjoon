import sys

N, M = map(int, sys.stdin.readline().split())
A, B = [], []

for row in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    A.append(row)

for col in range(N):
    col = list(map(int, sys.stdin.readline().split()))
    B.append(col)

for row in range(N):
    for col in range(M):
        print(A[row][col] + B[row][col], end = ' ')
    print()