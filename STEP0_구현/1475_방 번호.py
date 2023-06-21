import sys
from collections import defaultdict

n = sys.stdin.readline().strip()
dic = defaultdict(int)
for i in range(10):
    dic[str(i)] = 0

for num in n:
    if num == '6':
        num = '9'
    dic[num] += 1
    
max_num = max(dic, key=dic.get)
max_cnt = max(dic.values())
if max_num == '9':
    if max_cnt % 2 == 0:
        result = max_cnt // 2
    else:
        result = (max_cnt // 2) + 1
else:
    result = max_cnt

print(result)


