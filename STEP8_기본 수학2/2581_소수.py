import sys

def solve(num):
    if num < 2:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
num_list = []

for num in range(M, N+1):
    if solve(num):
        num_list.append(num)
    else:
        pass

if len(num_list):
    print(sum(num_list))
    print(min(num_list))
else:
    print("-1")