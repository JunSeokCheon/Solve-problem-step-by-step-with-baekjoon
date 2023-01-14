import sys

X = int(sys.stdin.readline())
N = int(sys.stdin.readline())
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    X = X - (a*b)

if X == 0:
    print("Yes")
else:
    print("No")