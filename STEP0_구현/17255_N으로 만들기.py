import sys

def dfs(num):
    global cnt

    if len(num) == 1:
        cnt += 1
        return
    num_split = set(list(num))
    if len(num_split) == 1:
        cnt += 1
        return
    else:
        dfs(num[1:])
        dfs(num[:-1])

n = sys.stdin.readline().strip()
cnt = 0
dfs(n)

print(cnt)