import sys

T = int(sys.stdin.readline())
for _ in range(T):
    R, S = map(str, sys.stdin.readline().split())
    sum_str = ''
    for mini_S in S:
        sum_str += mini_S * int(R)
    
    print(sum_str)