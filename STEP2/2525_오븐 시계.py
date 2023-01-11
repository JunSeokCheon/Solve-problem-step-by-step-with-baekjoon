import sys
A, B = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline())

A, B = A + C//60, B + C%60

if B >= 60:
    B_mok, B_rest = B//60, B%60
    A = A + B_mok
    if A >= 24:
        print(A-24, B_rest)
    else:
        print(A, B_rest)
else:
    if A >= 24:
        print(A-24, B)
    else:
        print(A, B)