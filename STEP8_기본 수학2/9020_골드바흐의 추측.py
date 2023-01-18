import sys

def solve(num):
    if num < 2:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True


T = int(sys.stdin.readline())
for _ in range(T):
    num = int(sys.stdin.readline())

    prev, next = num//2, num//2
    while(prev > 0):
        if solve(prev) and solve(next):
            print(prev, next, sep=" ")
            break
        else:
            prev -= 1
            next += 1