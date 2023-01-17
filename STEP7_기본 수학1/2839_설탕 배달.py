import sys

N = int(sys.stdin.readline())
count = 0

while(N > 0):
    if N % 5 == 0:
        count += N//5
        N -= (N//5 * 5)
    else:
        count += 1
        N -= 3

if N >= 0:
    print(count)
else:
    print("-1")