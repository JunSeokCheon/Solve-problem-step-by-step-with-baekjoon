import sys

A = int(sys.stdin.readline())
T = int(sys.stdin.readline())
opt = int(sys.stdin.readline())

bun = [0, 0]
order = -1
flag = False
repeat_idx = 2

while True:
    for i in range(2):
        # 뻔
        order += 1
        bun[0] += 1

        if bun[opt] == T:
            flag = True
            break

        # 데기
        order += 1
        bun[1] += 1

        if bun[opt] == T:
            flag = True
            break

    if flag == True:
        break
    
    # 뻔 X n
    for i in range(repeat_idx):
        order += 1
        bun[0] += 1

        if bun[opt] == T:
            flag = True
            break

    if flag == True:
        break
    
    # 데기 X n
    for i in range(repeat_idx):
        order += 1
        bun[1] += 1

        if bun[opt] == T:
            flag = True
            break
        
    if flag == True:
        break
    
    repeat_idx += 1

# 참가 인원 수로 나눈 나머지
print((order)%A)