import sys

N, M = map(int, sys.stdin.readline().split())
girl_group = {}

for _ in range(N):
    group = sys.stdin.readline().strip()
    number = int(sys.stdin.readline())
    girl_group[group] = []

    for _ in range(number):
        girl = sys.stdin.readline().strip()
        girl_group[group].append(girl)

for _ in range(M):
    question = sys.stdin.readline().strip()
    type = int(sys.stdin.readline())
    if type == 0:
        for name in sorted(girl_group[question]):
            print(name)
    elif type == 1:
        for key,value in girl_group.items():
            if question in value:
                print(key)