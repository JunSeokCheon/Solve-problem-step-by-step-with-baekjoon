import sys

S = sys.stdin.readline().strip()
result = ""
stack = []
flag = False

for mini_s in S:
    if mini_s == " ":
        while stack:
            result += stack.pop()
        result += mini_s
    elif mini_s == "<":
        while stack:
            result += stack.pop()
        result += mini_s
        flag = True
    elif mini_s == ">":
        result += mini_s
        flag = False
    elif flag:
        result += mini_s
    else:
        stack.append(mini_s)

while stack:
    result += stack.pop()

print(result)
