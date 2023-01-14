import sys

result_list = []

for _ in range(10):
    num = int(sys.stdin.readline())
    result_list.append(num%42)

print(len(set(result_list)))