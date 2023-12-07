import sys

n, digit = map(int, sys.stdin.readline().split())

num_dic = {}
for i in range(10):
    num_dic[i] = 0

for num in range(1, n+1):
    if num < 10:
        num_dic[num] += 1
    else:
        for mini_num in list(str(num)):
            num_dic[int(mini_num)] += 1

print(num_dic[digit])
