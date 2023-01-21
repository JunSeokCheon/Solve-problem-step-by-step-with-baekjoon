import sys

N = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().strip().split()))

result = sorted(list(set(n_list)))
n_dic = {result[i] : i for i in range(len(result))}
for answer in n_list:
    print(n_dic[answer], end=' ')