import sys
from itertools import combinations

expr = sys.stdin.readline().strip()
stack = []
remove_list = []
result = []

for i, value in enumerate(expr):
    if value == "(":
        stack.append(i)
    elif value == ")":
        remove_list.append((stack.pop(), i))

for i in range(1, len(remove_list)+1):
    remove = list(combinations(remove_list, i))
    for cases in remove:
        temp = list(expr)
        for case in cases:
            start = case[0]
            end = case[1]
            temp[start] = ""
            temp[end] = ""
        result.append("".join(temp))

result = list(set(result))
result.sort()

for answer in result:
    print(answer)