import sys

M, N = map(int, sys.stdin.readline().split())
num_list = []

def solve(num):
    if num < 2:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

for num in range(M, N+1):
    if solve(num):
        num_list.append(num)
    else:
        pass

num_list.sort()
for num in num_list:
    print(num)