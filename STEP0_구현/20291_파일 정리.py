import sys

N = int(sys.stdin.readline())
n_dic = {}

for _ in range(N):
    file = sys.stdin.readline().strip()
    extension = file.split('.')[1]
    if extension not in n_dic:
        n_dic[extension] = 1
    else:
        n_dic[extension] += 1

result = sorted(n_dic.items(), key = lambda x : x[0])
for answer in result:
    print(answer[0], answer[1], sep=' ')