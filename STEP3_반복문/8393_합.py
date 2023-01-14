import sys

n = int(sys.stdin.readline())
sum = 0

for num in range(1, n+1):
    sum += num

print(sum)