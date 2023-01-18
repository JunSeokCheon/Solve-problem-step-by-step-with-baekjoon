import sys

def solve(num):
    if num < 2:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
count = 0

for num in N_list:
    if solve(num):
        count += 1
    else:
        pass

print(count)