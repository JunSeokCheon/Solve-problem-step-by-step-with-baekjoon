import sys

N = sys.stdin.readline().strip()
n_list = []

for num in N:
    n_list.append(num)

n_list.sort(reverse=True)
print(int(''.join(n_list)))