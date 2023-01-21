import sys

n_list = []

for _ in range(5):
    n_list.append(int(sys.stdin.readline()))

n_list.sort()

print(sum(n_list)//5)
print(n_list[len(n_list)//2])