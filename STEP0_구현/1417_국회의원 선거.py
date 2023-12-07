import sys

n = int(sys.stdin.readline())
n_list = [int(sys.stdin.readline()) for _ in range(n)]
result = 0
goal = n_list[0]
n_list = n_list[1:]
n_list.sort(reverse=True)

if n == 1:
    print(result)
else:
    while n_list[0] >= goal:
        goal += 1
        n_list[0] -= 1
        result += 1
        n_list.sort(reverse=True)
    print(result)