import sys

stack = []

S = sys.stdin.readline().strip()
cnt = 0

for bracket in S:
    if bracket == "(":
        stack.append(bracket)
    elif bracket == ")" and len(stack) != 0 and stack[-1] == "(":
        stack.pop()
    else:
        cnt += 1

print(cnt+len(stack))