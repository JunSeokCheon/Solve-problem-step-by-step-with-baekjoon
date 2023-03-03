import sys

N, C = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
num_dic = {}

for num in num_list:
    if num not in num_dic:
        num_dic[num] = 1
    else:
        num_dic[num] += 1

result = sorted(num_dic.items(), key = lambda x : (-x[1]))
for answer in result:
    for i in range(1, answer[1]+1):
        print(str(answer[0]), end=' ')