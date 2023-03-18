import sys

N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))

N_list.sort()
N_list = N_list[::-1]

start = 0
end = N - 1
temp = []

while True:
    if start > end:
        break
    temp.append(N_list[start])
    temp.append(N_list[end])
    start += 1
    end -= 1

init = 0
answer = 0
for i in temp:
    if init < i:
        answer += i - init
    init = i

print(answer)