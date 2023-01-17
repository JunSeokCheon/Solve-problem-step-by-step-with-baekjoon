import sys

N = int(sys.stdin.readline())
cnt = 0
start = 1
grow = 0

while(True):
    cnt += 1
    if N <= start:
        print(cnt)
        break
    grow += 6
    start += grow
