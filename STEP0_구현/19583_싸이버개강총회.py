import sys

S, E, Q = map(str, sys.stdin.readline().split())
S_time = int(S[:2] + S[3:])
E_time = int(E[:2] + E[3:])
Q_time = int(Q[:2] + Q[3:])
result = set()
answer = 0

while True:
    try:
        time, name = map(str, sys.stdin.readline().split())
        T_time = int(time[:2] + time[3:])
        if S_time >= T_time:
            result.add(name)
        elif E_time <= T_time <= Q_time and name in result:
            result.remove(name)
            answer += 1
    except:
        break

print(answer)
