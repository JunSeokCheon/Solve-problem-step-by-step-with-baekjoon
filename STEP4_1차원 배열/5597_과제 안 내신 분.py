import sys

num_list = []
full_list = []

for _ in range(28):
    num_list.append(int(sys.stdin.readline()))

for i in range(1,31):
    full_list.append(i)
    
result = [x for x in full_list if x not in num_list]
print(min(result))
print(max(result))