import sys

S = sys.stdin.readline().strip()
result = []

for i in range(len(S)):
    result.append(S[i:])

result.sort()
for answer in result:
    print(answer)
    