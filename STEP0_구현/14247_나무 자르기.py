# 시간 초과
# import sys

# n = int(sys.stdin.readline())
# tree = list(map(int, sys.stdin.readline().split()))
# grow = list(map(int, sys.stdin.readline().split()))
# result = 0

# for _ in range(n):
#     tree = [x+y for x,y in zip(tree, grow)]
#     max_tree = max(tree)
#     max_tree_index = tree.index(max_tree)
#     result += max_tree
#     tree[max_tree_index] = 0

# print(result)

import sys

n = int(sys.stdin.readline())
tree = list(map(int, sys.stdin.readline().split()))
grow = list(map(int, sys.stdin.readline().split()))

sum_tree = sum(tree)
sort_grow = sorted(grow)

for i in range(n):
    sum_tree += sort_grow[i] * i

print(sum_tree)


