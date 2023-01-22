import sys

def solve(num):
    if num < 1:
        return 1
    else:
        return num * solve(num-1)

N = int(sys.stdin.readline())
result = solve(N)
print(result)