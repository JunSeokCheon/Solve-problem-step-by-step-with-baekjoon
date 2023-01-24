import sys


def recursion(S, l, r, c):
    if l >= r:
        return 1, c
    elif S[l] != S[r]:
        return 0, c
    else:
        c += 1
        return recursion(S, l+1, r-1, c)

T = int(sys.stdin.readline())
for _ in range(T):
    count = 1
    S = sys.stdin.readline().strip()
    result, count = recursion(S, 0, len(S)-1, count)
    print(result, count, sep=' ')