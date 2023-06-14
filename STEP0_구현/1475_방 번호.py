import sys
from collections import defaultdict

n = sys.stdin.readline().strip()
num_dic = defaultdict(int)
for i in range(10):
    num_dic[str(i)] = 0

for num in n:
    if num == '6':
        num = '9'
        num_dic[num] += 1
    else:
        num_dic[num] += 1

max_num = max(num_dic, key=num_dic.get)
max_cnt = max(num_dic.values())
if max_num == '9':
    if max_cnt % 2 == 0:
        result = max_cnt // 2
    else:
        result = (max_cnt // 2) + 1
else:
    result = max_cnt

print(result)
