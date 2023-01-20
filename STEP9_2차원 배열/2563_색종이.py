import sys

T = int(sys.stdin.readline())
paper = [[0 for _ in range(101)] for _ in range(101)]
area_sum = 0

for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1

for i in range(len(paper)):
    area_sum += sum(paper[i])

print(area_sum)