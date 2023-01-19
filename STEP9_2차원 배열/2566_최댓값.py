import sys

n_list = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
num_max = 0
num_x, num_y = 0, 0

for i in range(len(n_list)):
    for j in range(len(n_list[i])):
        if n_list[i][j] >= num_max:
            num_max = n_list[i][j]
            num_x = i
            num_y = j

print(num_max)
print(num_x+1, num_y+1, sep=' ')