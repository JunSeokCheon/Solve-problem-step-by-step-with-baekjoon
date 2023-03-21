import sys

N = int(sys.stdin.readline())
circle = []
stack = []

for i in range(N):
    x, r = map(int, sys.stdin.readline().split())
    circle.append((x-r, i, "open"))
    circle.append((x+r, i, "close"))

circle.sort()

for i in range(N):
    type = circle[i][2]

    if type == "open":
        stack.append(circle[i])
    else:
        if stack[-1][2] == "open":
            if circle[i][1] == stack[-1][1]:
                stack.pop()
            else:
                print("NO")
                exit(0)

print("YES")