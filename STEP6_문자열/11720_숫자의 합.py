import sys

N = int(sys.stdin.readline())
N_num = sys.stdin.readline().strip()
N_sum = 0

for num in N_num:
    if int(num) == 0:
        continue
    N_sum += int(num)

print(N_sum)