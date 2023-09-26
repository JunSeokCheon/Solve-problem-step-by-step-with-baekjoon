import sys

n = int(sys.stdin.readline())
n_list = [list(map(str, sys.stdin.readline().strip())) for _ in range(n)]
row = 0
col = 0

for i in range(n):
    row_check = ''.join(n_list[i])
    for check in row_check.split('X'):
        if len(check) >= 2:
            row += 1
            
    col_check = ''
    for j in range(n):
        col_check += n_list[j][i]
    
    for check in col_check.split('X'):
        if len(check) >= 2:
            col += 1
    
print(row, col)
