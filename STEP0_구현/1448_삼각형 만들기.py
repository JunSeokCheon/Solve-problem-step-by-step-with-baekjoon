import sys

N = int(sys.stdin.readline())
flag = False
tri = []

for _ in range(N):
    piew = int(sys.stdin.readline())
    tri.append(piew)

tri.sort(reverse=True)
for i in range(len(tri)-2):
    if tri[i] < tri[i+1] + tri[i+2]:
        result = tri[i] + tri[i+1] + tri[i+2]
        print(result)
        flag = True
        break

if flag == False:
    print(-1)