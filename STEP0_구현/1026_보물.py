import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
result = 0

a.sort()
b.sort(reverse=True)

for num1, num2 in zip(a,b):
    result += num1*num2

print(result)