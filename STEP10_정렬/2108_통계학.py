import sys

n_list = []
N = int(sys.stdin.readline())
n_dic = {}

for _ in range(N):
    num = int(sys.stdin.readline())
    n_list.append(num)
    
    if num not in n_dic:
        n_dic[num] = 1
    else:
        n_dic[num] += 1

value_max = max(n_dic.values())
mode_list = []
for key, value in n_dic.items():
    if value == value_max:
        mode_list.append(key)

print(round(sum(n_list)/N))
n_list.sort()
mode_list.sort()
print(n_list[len(n_list)//2])
if len(mode_list) == 1:
    print(mode_list[0])
else:
    print(mode_list[1])
print(max(n_list)-min(n_list))