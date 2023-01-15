import sys

A, B = map(str, sys.stdin.readline().split())

if A[::-1] > B[::-1]:
    print(A[::-1])
else:
    print(B[::-1])