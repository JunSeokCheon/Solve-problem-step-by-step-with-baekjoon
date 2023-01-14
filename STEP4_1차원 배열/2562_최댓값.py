import sys

N_list = []

for _ in range(9):
    N_list.append(int(sys.stdin.readline()))

list_max = max(N_list)
print(list_max)

for index, num in enumerate(N_list):
    if num == list_max:
        print(index+1)
            