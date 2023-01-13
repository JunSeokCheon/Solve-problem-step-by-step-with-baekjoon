import sys

N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
new_list = []

N_max = max(N_list)

for num in N_list:
    new_list.append(num/N_max*100)

print(sum(new_list)/N)