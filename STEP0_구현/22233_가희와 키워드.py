import sys

n, m = map(int, sys.stdin.readline().split())
n_set = set()
result = 0

for _ in range(n):
    n_set.add(sys.stdin.readline().strip())

for _ in range(m):
    keyword = sys.stdin.readline().strip()
    for key in keyword.split(","):
        try:
            n_set.remove(key)
        except:
            pass
    print(len(n_set))