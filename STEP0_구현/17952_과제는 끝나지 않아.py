import sys

n = int(sys.stdin.readline())
total_task = []
result = 0
for _ in range(n):
    mini_task = list(map(int, sys.stdin.readline().split()))
    if mini_task[0] == 1:
        # 점수, 시간
        total_task.append((mini_task[1], mini_task[2]))
    
    if total_task:
        score, time = total_task.pop()
        time -= 1

        if time == 0:
            result += score
        else:
            total_task.append((score, time))

print(result)
