import sys

n = sys.stdin.readline().strip()
n_len = len(n)
result = 0

if n_len == 1:
    print(n)
    exit(0)
else:
    for i in range(1, n_len):  
        result += (9*(10**(i-1))) * (i)
    
    rest = int(n) - (10**(n_len-1)) + 1
    result += (rest * n_len)

print(result)
