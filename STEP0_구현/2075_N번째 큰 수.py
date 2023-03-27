import sys

n = int(sys.stdin.readline())
result = []

for _ in range(n):
    result += map(int, sys.stdin.readline().split())
    result = sorted(result, reverse=True)[:n]

print(result[n-1])
