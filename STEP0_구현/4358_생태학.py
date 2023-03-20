import sys
from collections import defaultdict

dict = defaultdict(int)
total_tree = 0

while True:
    tree = sys.stdin.readline().strip()
    if not tree:
        break
    dict[tree] += 1
    total_tree += 1

tree_name = sorted(dict.keys())

for name in tree_name:
    print("{} {:.4f}".format(name, dict[name]/total_tree*100))
